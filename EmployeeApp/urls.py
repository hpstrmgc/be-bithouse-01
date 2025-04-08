from django.urls import path
from . import views

urlpatterns = [
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('upload-certification/', views.upload_certification, name='upload_certification'),
]