from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index_page_view(request):
    text = 'Hello world'
    return HttpResponse(text)

def product_list(request):
    products =Product.objects.all()
    return render(request,'testapp/product_list.html',context={'products':products})