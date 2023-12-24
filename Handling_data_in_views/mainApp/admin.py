from django.contrib import admin
from .models import product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','desc','price','qty']
admin.site.register(product,ProductAdmin)
