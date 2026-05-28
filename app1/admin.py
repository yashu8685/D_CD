from django.contrib import admin
from app1.models import student
# Register your models here.

class Sadmin(admin.ModelAdmin):
    list_display=['sid','sname','smark','ssub']

admin.site.register(student,Sadmin)

