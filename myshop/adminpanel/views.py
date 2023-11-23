from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def admin_product_list(request):
    products = Product.objects.all()
    return render(request, 'adminpanel/product_list.html', {'products': products})



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')  # Перенаправление после успешного создания товара
    else:
        form = ProductForm()  # Создание пустой формы для GET-запроса

    return render(request, 'adminpanel/product_form.html', {'form': form})



def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm(instance=product)  # Использование экземпляра продукта для инициализации формы

    return render(request, 'adminpanel/product_form.html', {'form': form, 'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('admin_product_list')