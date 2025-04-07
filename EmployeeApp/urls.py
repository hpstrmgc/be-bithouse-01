from django.urls import path
from . import views

urlpatterns = [
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
]