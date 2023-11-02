from django.contrib import admin
from .models import Customer, Product, Order, Prescription, Payment, Category, Manufacturer, Employee, ShippingAddress, Review

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Prescription)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Employee)
admin.site.register(ShippingAddress)
admin.site.register(Review)
