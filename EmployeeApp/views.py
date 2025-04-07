from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Certification
from .forms import EmployeeForm  # Pastikan Anda sudah membuat EmployeeForm di forms.py

def employee_detail(request, employee_id):
    # Ambil data employee berdasarkan ID
    employee = get_object_or_404(Employee, employee_id=employee_id)
    
    # Ambil data sertifikasi yang terkait dengan employee
    certifications = Certification.objects.filter(employee=employee)
    
    # Jika metode POST, proses formulir
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', employee_id=employee.employee_id)  # Redirect ke halaman detail
    else:
        form = EmployeeForm(instance=employee)  # Formulir untuk data employee

    # Kirim data ke template
    context = {
        'employee': employee,
        'certifications': certifications,
        'form': form,  # Tambahkan formulir ke konteks
    }
    return render(request, 'employee_detail.html', context)