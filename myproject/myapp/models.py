from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=15)

    USERNAME_FIELD = 'name'
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
class Order(models.Model):
    User = models.ForeignKey('User', on_delete=models.CASCADE, default=1)
    address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20)

    def __str__(self):
        return f"Order ID: {self.id}"

class Prescription(models.Model):
    User = models.ForeignKey('User', on_delete=models.CASCADE,default=1)
    doctor_name = models.CharField(max_length=100)
    prescription_date = models.DateField()
    expiry_date = models.DateField()
    medication_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Prescription ID: {self.id}"

class Payment(models.Model):
    order = models.OneToOneField('Order', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment ID: {self.id}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ShippingAddress(models.Model):
    User = models.ForeignKey('User', on_delete=models.CASCADE,default=1)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"Shipping Address ID: {self.id}"

class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    User = models.ForeignKey('User', on_delete=models.CASCADE ,default=1)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review ID: {self.id}"
