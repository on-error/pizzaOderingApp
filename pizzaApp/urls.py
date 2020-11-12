"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import acceptOrder,rejectOrder,adminOrders,userOrders,placeorder,logoutCustomer, index, addPizza, adminLoginView, adminHomeLogin, authenticateAdmin, adminLogout, deletePizza, signupUser, loginView, userAuthenticate, loginWelcome

urlpatterns = [
    path('admin/', adminLoginView, name = 'adminlogin'),
    path('authenticate/', authenticateAdmin),
    path('admin/homepage', adminHomeLogin, name = 'adminHomepage'),
    path('adminLogout/', adminLogout),
    path('addpizza/', addPizza),
    path('deletePizza/<int:pizzapk>/', deletePizza),
    path('', index, name = 'index'),
    path('signupuser/', signupUser),
    path('login/', loginView , name = 'login'),
    path('login/authenticate/', userAuthenticate),
    path('login/welcome/' , loginWelcome, name='loginWelcome'),
    path('logout/', logoutCustomer, name='logout'),
    path('placeorder/', placeorder),
    path('userOrders/', userOrders),
    path('adminOrders/', adminOrders, name = 'adminOrders'),
    path('acceptOrder/<int:orderpk>/', acceptOrder),
    path('rejectOrder/<int:orderpk>/', rejectOrder),
    
]
