from django.urls import path
from .views import home_page, product_detail, \
    add_to_cart, user_cart, delete_cart_item, \
    plus_cart_item, minus_cart_item, rasmiylashtirish, pay_checkout


urlpatterns = [
    path('', home_page, name='home'),
    path('cart/', user_cart, name='user_cart'),
    path('checkout/', rasmiylashtirish, name='checkout'),
    path('checkout-pay/', pay_checkout, name='pay_checkout'),

    path('<int:id>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('delete-cart-item/<int:id>/', delete_cart_item, name='delete_cart_item'),
    path('plus-cart-item/<int:id>/', plus_cart_item, name='plus_cart_item'),
    path('minus-cart-item/<int:id>/', minus_cart_item, name='minus_cart_item'),
]
