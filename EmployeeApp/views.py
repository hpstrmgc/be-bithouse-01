from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST
from .models import Employee, Certification, Departement
from .forms import EmployeeForm, CertificationForm
import os

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    departments = Departement.objects.all()

    certifications = Certification.objects.filter(employee=employee)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', employee_id=employee.employee_id)
    else:
        form = EmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'certifications': certifications,
        'form': form,
        'departments': departments,
    }
    return render(request, 'employee_detail.html', context)

@require_POST
def upload_profile_photo(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)

    photo = request.FILES.get('profile_picture')
    if not photo:
        messages.error(request, "No file selected.")
        return redirect('employee_detail', employee_id=employee_id)

    if photo.content_type not in ['image/jpeg', 'image/png']:
        messages.error(request, "Only JPEG and PNG images are allowed.")
        return redirect('employee_detail', employee_id=employee_id)

    if photo.size > 2 * 1024 * 1024:  # 2MB
        messages.error(request, "The image file size must not exceed 2MB.")
        return redirect('employee_detail', employee_id=employee_id)

    employee.profile_picture = photo
    employee.save()
    messages.success(request, "Profile photo uploaded successfully.")
    return redirect('employee_detail', employee_id=employee_id)

def delete_profile_picture(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    if employee.profile_picture and os.path.isfile(employee.profile_picture.path):
        os.remove(employee.profile_picture.path)
        employee.profile_picture = None
        employee.save()
    return redirect('employee_detail', employee_id=employee_id)

def upload_certification(request):
    if request.method == 'POST':
        cert_id = request.POST.get('certification_id')
        print(f"Received certification_id: {cert_id}")  # Log untuk memastikan certification_id diterima

        if not cert_id:
            print("Certification ID is missing.")  # Log jika certification_id tidak ada
            return HttpResponse("Certification ID is missing.", status=400)

        certification = get_object_or_404(Certification, certification_id=cert_id)
        print(f"Certification object found: {certification}")  # Log untuk memastikan objek ditemukan

        form = CertificationForm(request.POST, request.FILES, instance=certification)
        print(f"Form data: {form.data}")  # Log untuk melihat data formulir
        print(f"Form files: {form.files}")  # Log untuk melihat file yang diunggah

        if form.is_valid():
            form.save()
            print(f"File saved at: {certification.file.path}")  # Log lokasi file yang disimpan
            return redirect('employee_detail', employee_id=certification.employee.employee_id)
        else:
            print("Form is invalid.")  # Log jika formulir tidak valid
            return HttpResponse("Invalid file type. Only .docx files are allowed.", status=400)
    print("Invalid request method.")  # Log jika metode request bukan POST
    return HttpResponse("Invalid request method.", status=405)

def add_certification(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = Employee.objects.get(employee_id=employee_id)

        Certification.objects.create(
            employee=employee,
            name=request.POST.get('name'),
            number=request.POST.get('number'),
            date_issued=request.POST.get('date_issued'),
            verify_period=request.POST.get('verify_period'),
            description=request.POST.get('description')
        )
        return redirect('employee_detail', employee_id=employee_id)
    return HttpResponse("Invalid request method.", status=405)

def delete_certification(request, cert_id):
    certification = get_object_or_404(Certification, certification_id=cert_id)
    employee_id = certification.employee.employee_id
    if certification.file and os.path.isfile(certification.file.path):
        os.remove(certification.file.path)
    certification.delete()
    return redirect('employee_detail', employee_id=employee_id)

def index(request):
    return HttpResponse("Welcome to the EmployeeApp!")