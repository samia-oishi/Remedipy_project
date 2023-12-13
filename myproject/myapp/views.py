from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):

    return render(request, 'index.html')


def products(request):
    return render(request,'products.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):

    return render(request,'service.html')


def login(request):

    return render(request, "login.html", {})


def register_view(request):
    form = CreateUserForm()
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'register.html',context)
    #
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         user_name = form.cleaned_data.get("user_name")
    #         user_email = form.cleaned_data.get("user_email")
    #         user_password = form.cleaned_data.get("u_password")
    #
    #         user = User.objects.create_user(username=user_name, email=user_email, password=user_password)
    #         user.save()
    #
    #         authenticated_user = authenticate(request, username=user_name, password=user_password)
    #
    #         if authenticated_user is not None:
    #             auth_login(request, authenticated_user)
    #             messages.success(request, "Your account has been successfully created.")
    #             return redirect("index")
    #         else:
    #             messages.error(request, "User registration failed. Please try again.")

    return render(request, "register.html", {"form": form})
def logout(request):

    return redirect('index')

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

