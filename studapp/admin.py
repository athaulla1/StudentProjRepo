from django.contrib import admin
from studapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['sid','sname','sm1','sm2','sm3','tot']
admin.site.register(Student,StudentAdmin)
