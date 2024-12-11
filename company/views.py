from django.shortcuts import render, redirect
from .forms import AdminRegistrationForm, EmployeeRegistrationForm, CompanyForm
from .models import Admin, Employee, Company


def register_admin(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу логина
    else:
        form = AdminRegistrationForm()
    return render(request, 'company/register_admin.html', {'form': form})

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'company/register_employee.html', {'form': form})


def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем компанию в базу данных
            return redirect('company_list')  # Перенаправляем на страницу списка компаний (или на другую страницу)
    else:
        form = CompanyForm()
    return render(request, 'company/add_company.html', {'form': form})

def company_list(request):
    companies = Company.objects.all()  # Получаем все компании
    return render(request, 'company/company_list.html', {'companies': companies})

