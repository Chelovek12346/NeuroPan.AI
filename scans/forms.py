from django import forms
from .models import Scan


class ScanUploadForm(forms.ModelForm):
    class Meta:
        model = Scan
        fields = ['file']
