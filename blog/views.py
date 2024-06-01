from django.shortcuts import render
from django.views import View
from .models import Products
# Create your views here.


class ProductsView(View):
    def get(self, request):
        products =