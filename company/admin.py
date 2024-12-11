from django.contrib import admin

from company.models import Admin, Employee, Company, RegistrationRequest

# Register your models here.
# Регистрируем модели
admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(RegistrationRequest)