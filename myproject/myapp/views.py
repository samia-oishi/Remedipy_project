from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    return render(request,'index.html')
def products(request):
    return render(request,'products.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def service(request):

    return render(request,'service.html')
def login(request):

    return render(request, "login.html", {})
def register(request):

    return render(request, "register.html", {})

def cart(request):
    return render(request,'cart.html')
from django.shortcuts import render
from .models import User, Product, Order, Prescription, Payment, Category, Manufacturer, Employee, ShippingAddress, Review

def product_list(request):
    #products = Product.objects.all()
    categories = Category.objects.all()
    #return render(request, 'product_list.html', {'products': products})
    return render(request, 'product_list.html', {'categories': categories})
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'product_details.html', context)
def User_orders(request, User_id):
    Users = User.objects.get(id=User_id)
    orders = Order.objects.filter(User=User)
    return render(request, 'customer_orders.html', {'User': Users, 'orders': orders})

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        manufacturer_id = request.POST['manufacturer']
        category_id = request.POST['category']

        manufacturer = Manufacturer.objects.get(id=manufacturer_id)
        category = Category.objects.get(id=category_id)

        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            manufacturer=manufacturer,
            category=category
        )

        return render(request, 'product_added.html', {'product': product})

    manufacturers = Manufacturer.objects.all()
    categories = Category.objects.all()
    return render(request, 'add_product.html', {'manufacturers': manufacturers, 'categories': categories})

#add more...

