from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('analyze/<str:modality>/', views.analyze_view, name='analyze'),
    path('result/<int:pk>/', views.result_view, name='scan_result'),
]
