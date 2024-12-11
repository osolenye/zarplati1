from django.shortcuts import render, redirect
from .forms import AdminRegistrationForm, EmployeeRegistrationForm, CompanyForm, RegistrationRequestForm, PaymentForm
from .models import Admin, Employee, Company, Payment


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


def registration_request(request):
    if request.method == 'POST':
        form = RegistrationRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем запрос в базе данных
            return redirect('company_list')  # Перенаправляем на страницу списка компаний или другую нужную страницу
    else:
        form = RegistrationRequestForm()

    return render(request, 'company/registration_request.html', {'form': form})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем платеж в базе данных
            return redirect('payment_list')  # Перенаправляем на страницу списка платежей или другую нужную страницу
    else:
        form = PaymentForm()

    return render(request, 'company/add_payment.html', {'form': form})

def payment_list(request):
    payments = Payment.objects.all()  # Получаем все платежи
    return render(request, 'company/payment_list.html', {'payments': payments})