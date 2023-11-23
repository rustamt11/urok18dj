from django.shortcuts import render, get_object_or_404, redirect

from adminpanel.models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'customer/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'customer/product_detail.html', {'product': product})

def buy_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.purchase_status = True
    product.delete()
    return redirect('product_list')
