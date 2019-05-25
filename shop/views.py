# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from cart.cart import Cart

def product_list(request, category_slug=None):
    if request.user.is_authenticated:
        category = None
        categories = Category.objects.all()
        # products = Product.objects.filter(available=True)
        products = Product.objects.all()
        cart = Cart(request)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category)

        context = {
            'category': category,
            'categories': categories,
            'products': products,
            'cart': cart,
        }
        return render(request, 'shop/product/list.html', context)
    else:
        return redirect('user/signin/')


def product_detail(request, id, slug):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id, slug=slug) #, available=True
        cart_product_form = CartAddProductForm()
        cart = Cart(request)
        context = {
            'product': product,
            'cart_product_form': cart_product_form,
            'cart': cart,
        }
        return render(request, 'shop/product/detail.html', context)
    else:
        return redirect('user/signin/')
    
    
