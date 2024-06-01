from django.contrib import admin
from .models import Products, Comments, Saved
# Register your models here.


admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(Saved)