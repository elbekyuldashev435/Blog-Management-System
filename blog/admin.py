from django.contrib import admin
from .models import Products, Comments, Saved, About
# Register your models here.


admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(Saved)
admin.site.register(About)