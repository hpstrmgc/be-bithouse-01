from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('upload-certification/', views.upload_certification, name='upload_certification'),
    path('add-certification/', views.add_certification, name='add_certification'),
    path('delete-certification/<int:cert_id>/', views.delete_certification, name='delete_certification'),
    path('employee/<int:employee_id>/delete_photo/', views.delete_profile_picture, name='delete_photo'),
    path('employee/<int:employee_id>/upload-photo/', views.upload_profile_photo, name='upload_profile_photo'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)