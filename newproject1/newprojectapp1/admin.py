from django.contrib import admin
from .models import student
from .models import teacher
# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
