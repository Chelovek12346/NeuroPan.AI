from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Scan
from .forms import ScanUploadForm
from ml.predictor import analyze_scan


def landing_view(request):
    return render(request, 'scans/landing.html')


@login_required
def dashboard_view(request):
    scans = Scan.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'scans/dashboard.html', {'scans': scans})


@login_required
def analyze_view(request, modality):
    modality = modality.lower()
    if modality not in ['ct', 'mri']:
        raise Http404("Unknown modality")

    if request.method == 'POST':
        form = ScanUploadForm(request.POST, request.FILES)
        if form.is_valid():
            scan = form.save(commit=False)
            scan.user = request.user
            scan.modality = modality
            scan.save()


            result = analyze_scan(scan.file.path, scan.modality)
            scan.result = result
            scan.save()

            return redirect('scan_result', pk=scan.pk)
    else:
        form = ScanUploadForm()

    return render(request, 'scans/analyze.html', {
        'form': form,
        'modality': modality,
    })


@login_required
def result_view(request, pk):
    scan = get_object_or_404(Scan, pk=pk, user=request.user)
    return render(request, 'scans/result.html', {'scan': scan})
