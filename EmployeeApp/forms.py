from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # Gunakan semua field dari model Employee
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date'}),  # Date picker untuk join_date
            'end_date': forms.DateInput(attrs={'type': 'date'}),  # Date picker untuk end_date
        }