from django.contrib import admin
from app.models import Medical,Product

class MedicalAdmin(admin.ModelAdmin):
    # list_display = ['Patient_name','Email','Mobile','Date','Department_name','Doctor_name']
    list_display = ('Patient_name','Email','Mobile','Date','Department_name','Doctor_name')
    
    list_filter = ['Doctor_name','Department_name']

admin.site.register(Medical,MedicalAdmin)
admin.site.site_header="Medical Administrator"
admin.site.site_title="Medical Admin"
admin.site.index_title="Medical "

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","status")
    
admin.site.register(Product,ProductAdmin)