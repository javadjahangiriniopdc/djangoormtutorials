from django.contrib import admin

# Register your models here.
from myapp.models import Student, Teacher

admin.site.register(Student)
admin.site.register(Teacher)
