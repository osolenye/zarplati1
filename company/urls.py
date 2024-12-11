from django.urls import path
from . import views

urlpatterns = [
    path('register/admin/', views.register_admin, name='register_admin'),
    path('register/employee/', views.register_employee, name='register_employee'),
    path('add_company/', views.add_company, name='add_company'),  # Путь для добавления компании
    path('companies/', views.company_list, name='company_list'),  # Страница со списком компаний

]