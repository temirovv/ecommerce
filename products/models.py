from django.db import models
from users.models import CustomUser



class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = "Mahsulotlar"
        ordering = ['id']

    def __str__(self):
        return self.name

    @property
    def price_with_discount(self):
        return self.price - self.price * (self.discount/100)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image of {self.product.name}"

class Color(models.Model):
    name = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def get_price(self):
        return self.quantity * self.product.price_with_discount


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)    
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    shipping_address = models.CharField(max_length=255, null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
