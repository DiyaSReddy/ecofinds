from django.shortcuts import render, get_object_or_404
from .models import Product  # make sure Product model exists in models.py

# Homepage view
def home(request):
    return render(request, 'marketplace/home.html')

# Product listing view
def product_list(request):
    products = Product.objects.all()
    return render(request, 'marketplace/product_list.html', {'products': products})

# Product detail view
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'marketplace/product_detail.html', {'product': product})

