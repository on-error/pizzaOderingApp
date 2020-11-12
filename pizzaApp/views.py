from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel, CustomerModel, OrderModel
from django.contrib.auth.models import User

# Create your views here.
def adminLoginView(request):
    return render(request, 'adminlogin.html')

def authenticateAdmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username, password = password)
    if user is not None and user.username == "admin":
        #welcome to admin home page
        login(request, user)
        return redirect('adminHomepage')
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
        return redirect('adminlogin')

def adminHomeLogin(request):
    details = PizzaModel.objects.all()
    context = {'pizzas':details}
    return render(request, 'adminhomepage.html', context)

def adminLogout(request):
    logout(request)
    return redirect('adminlogin')

def addPizza(request):
    name = request.POST['name']
    price = request.POST['price']
    PizzaModel(name = name, price = price).save()
    return redirect('adminHomepage')

def deletePizza(request, pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect("adminHomepage")

def index(request):
    return render(request,'index.html')

def signupUser(request):
    username = request.POST['username']
    password = request.POST['password']
    mobileno = request.POST['mobileno']
    # if user already exists 
    if User.objects.filter(username = username).exists():
        messages.add_message(request, messages.ERROR, "Username Already exists")
        return redirect('index')
    # if user dosent exits
    User.objects.create_user(username = username, password = password).save()
    lastobject = len(User.objects.all()) - 1
    CustomerModel(userid=User.objects.all()[int(lastobject)].id, username=username, phone_no = mobileno).save()
    messages.add_message(request, messages.ERROR, "Account Created Successfully")
    return redirect('index')


def loginView(request):
    return render(request, 'loginview.html')

def userAuthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username, password = password)
    if user is not None:
        #welcome to admin home page
        login(request, user)
        return redirect('loginWelcome')
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
        return redirect('login')

def loginWelcome(request):
    if not request.user.is_authenticated:
        return redirect('login')
    username = request.user.username
    pizzas = PizzaModel.objects.all()
    context = {'username' : username, 'pizzas' : pizzas}
    return render(request, 'loginwelcome.html', context)

def logoutCustomer(request):
    logout(request)
    return redirect('login')

def placeorder(request):
    username = request.user.username 
    #mobileno = CustomerModel.objects.filter(userid = request.user.id).phone_no
    address = request.POST['address']
    ordereditems = ""

    for pizza in PizzaModel.objects.all():
        pizzaid = pizza.id
        name = pizza.name
        price = pizza.price
        quantity = request.POST.get(str(pizzaid), " ")
        print(quantity)
        if str(quantity) != "0" and str(quantity) != " ":
            ordereditems = ordereditems + name + " Price : " + str(int(quantity)*int(price)) + " Quantity : " + quantity + "  "
    print(ordereditems)
    OrderModel(username = username, address= address, ordereditems = ordereditems).save()
    messages.add_message(request, messages.SUCCESS, "Order Placed Successfully")
    return redirect('loginWelcome')

def userOrders(request):
    orders = OrderModel.objects.filter(username = request.user.username)
    context = {'orders' : orders}
    return render(request, 'userorder.html', context)


def adminOrders(request):
    orders = OrderModel.objects.all()
    context = {'orders' : orders}
    return render(request, 'orderadmin.html', context)

def acceptOrder(request, orderpk):
    order = OrderModel.objects.get(id = orderpk)
    order.status = "Accepted"
    order.save()
    return redirect('adminOrders')

def rejectOrder(request, orderpk):
    order = OrderModel.objects.get(id = orderpk)
    order.status = "Rejected"
    order.save()
    return redirect('adminOrders')
