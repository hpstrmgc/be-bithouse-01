from django import forms
from .models import Employee, Certification

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' 
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date'}),  
            'end_date': forms.DateInput(attrs={'type': 'date'}), 
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'accept': '.docx'}),  # Hanya terima file .docx
        }