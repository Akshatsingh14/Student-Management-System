from django.contrib import admin
from .models import Sdata

# Register your models here.
@admin.register(Sdata)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','Name','Qualification','Gender','YOP','Age','Skills','DOB','Address','Mock_Rating','Department']
    list_display_links = ['Name']