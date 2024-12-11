from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Admin, Employee, Company


class AdminRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Admin
        fields = ['username', 'password', 'company', 'access_level']

    def save(self, commit=True):
        admin = super().save(commit=False)
        admin.password = make_password(self.cleaned_data['password'])  # Hash the password manually
        if commit:
            admin.save()
        return admin


class EmployeeRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['username', 'first_name', 'last_name', 'patronymic', 'salary', 'phone_number', 'position', 'company']

    def save(self, commit=True):
        employee = super().save(commit=False)
        # Хешируем пароль
        employee.password = make_password(self.cleaned_data['password'])
        if commit:
            employee.save()
        return employee

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'employee_count']  # Поля для ввода информации о компании