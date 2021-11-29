from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from home.models import Contact
from django.contrib.auth import logout, authenticate, login
# Create your views here.

data = {'name': 'Sign in'}
def index(request):
    if request.user.is_anonymous:
        return redirect("/signin") 
    return render(request,'index.html',data)

def about(request):
    return render(request,'about.html',data)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your messages has been sent!')
    return render(request,'contact.html',data)

def shop(request):
    if request.user.is_anonymous:
        return redirect("/signin")
    return render(request,'shop.html',data)

def orders(request):
    if request.user.is_anonymous:
        return redirect("/signin")
    return render(request,'orders.html',data)

def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            data['name']=username
            messages.success(request, 'Welcome,{}!'.format(username))
            return redirect("/home")

        else:
            # No backend authenticated the credentials
            messages.warning(request, 'Invalid password!')
            return render(request, 'signin.html',data)
    return render(request,'signin.html',data)

def signout(request):
    logout(request)
    data['name']='Sign in'
    return redirect("/signin")

