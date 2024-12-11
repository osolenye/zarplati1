from django.db import models

# Модель Фирма
class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компании')
    employee_count = models.IntegerField(verbose_name='Количество сотрудников')

    def __str__(self):
        return self.name

# Модель Сотрудник
class Employee(models.Model):
    username = models.CharField(max_length=100, unique=True, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', blank=True)
    salary = models.FloatField(verbose_name='Зарплата')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    position = models.CharField(max_length=100, verbose_name='Должность')
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE, verbose_name='Компания')
    password = models.CharField(max_length=255, verbose_name='Пароль')  # Хешированный пароль

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Модель Администратор
class Admin(models.Model):
    username = models.CharField(max_length=100, unique=True, verbose_name='Имя пользователя')
    password = models.CharField(max_length=255, verbose_name='Пароль')  # Пароль будет хэширован
    company = models.ForeignKey(Company, related_name='admins', on_delete=models.CASCADE, verbose_name='Компания')
    access_level = models.CharField(max_length=50, choices=[('admin', 'Админ'), ('moderator', 'Модератор')], verbose_name='Уровень доступа')

    def __str__(self):
        return self.username
