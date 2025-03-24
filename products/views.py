from django.shortcuts import render, redirect
from .models import Product, Category, Cart, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required


def home_page(request):
    q = request.GET.get('q')
    category = request.GET.get('category')

    if q:
        mahsulotlar = Product.objects.filter(name__icontains=q)
    else:
        mahsulotlar = Product.objects.all()

    if category:
       mahsulotlar = mahsulotlar.filter(category__name__icontains=category)
  
    kategoriyalar = Category.objects.all()

    if request.user.is_authenticated:
        if Cart.objects.filter(user=request.user).exists():
            cart = Cart.objects.get(user=request.user)
            cartlar = CartItem.objects.filter(cart=cart)

    context = {
        'kategoriyalar': kategoriyalar,
        'mahsulotlar': mahsulotlar
    }

    return render(request, 'home.html', context=context)


def product_detail(request, id):
    mahsulot = Product.objects.get(id=id)
    return render(request, 'product-detail.html', context={'product': mahsulot})


@login_required
def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    user = request.user

    cart, cart_created = Cart.objects.get_or_create(user=user)
    cart_item, cart_item_created = CartItem.objects.get_or_create(
        cart=cart, product=product
    )

    if not cart_item_created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
        
    cart_item.save()

    return redirect('product_detail', id=id)


@login_required
def user_cart(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    jami_narx = sum(
        [
            cart_item.product.price_with_discount * cart_item.quantity for cart_item in cart_items
        ]
    )

    context = {
        'cart_items': cart_items,
        'jami': jami_narx
    }

    return render(request, 'cart.html', context=context)


@login_required
def plus_cart_item(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('user_cart')

@login_required
def minus_cart_item(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity -= 1
    cart_item.save()

    return redirect('user_cart')


@login_required
def delete_cart_item(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()

    return redirect('user_cart')


@login_required
def rasmiylashtirish(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)

    order = Order.objects.create(
        user=user
    )

    total_price = 0
    for cart_item in cart_items:
        price = cart_item.get_price
        total_price += price
    
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            price=price
        )
    
    context = {
        'order_id': order.id,
        'total_price': total_price
    }

    return render(request, 'rasmiylashtirish.html', context=context)


@login_required
def pay_checkout(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_paid = True
    order.save()

    cart = Cart.objects.get(user=request.user)
    cart.delete()

    return redirect('home')

