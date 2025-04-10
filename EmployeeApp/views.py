from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Employee, Certification
from .forms import EmployeeForm, CertificationForm
from django.shortcuts import redirect
from .models import Certification, Employee

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    
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
    }
    return render(request, 'employee_detail.html', context)

def upload_certification(request):
    if request.method == 'POST':
        cert_id = request.POST.get('certification_id')

        if not cert_id:
            return HttpResponse("Certification ID is missing.", status=400)

        certification = get_object_or_404(Certification, certification_id=cert_id)
        form = CertificationForm(request.POST, request.FILES, instance=certification)

        if form.is_valid():
            form.save()
            return redirect('employee_detail', employee_id=certification.employee.employee_id)
        else:
            return HttpResponse("Invalid file type. Only .docx files are allowed.", status=400)
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