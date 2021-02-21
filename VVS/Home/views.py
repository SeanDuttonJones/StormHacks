from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,HttpResponseRedirect
from Website_Settings import settings
from django.contrib.messages import error
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import Register,Login,Shopper,Business


# Create your views here.

def home_page(request):
    homeHTML = 'Maps/index.html'
    return render(request,homeHTML)

def login_page(request):
    """
    Get username and password from the form, and if its legal, then let you login
    """
    loginHTML = 'Home/login.html'

    Form_Login = Login()

    if request.method == 'POST':
        Form_Login = Login(request.POST)
        if Form_Login.is_valid():
            username = Form_Login.cleaned_data['username']
            password = Form_Login.cleaned_data['password']
            User = authenticate(username = username,password = password)
            if User is not None: # IF User is in database, then log in, else redirect to login//do nothing
                login(request,User)
                return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
            else:
                error(request,"User or Password not correct")
                return redirect('/login/')
        else:
            error(request,"User or Password not correct")
            return redirect('/login/')
            
                
    context = {
        'form_login': Form_Login,
    }
    return  render(request,loginHTML,context)

def logout_page(request):
    logout(request)
    logoutHTML = 'Home/logout.html'
    return render(request,logoutHTML)

def registration_page(request):
    """
    Create Username and Password from the form, and if its legal
    It'll log you in, and register you 
    """
    Form_Registration = Register()

    registerHTML = 'Home/register.html'

    if request.method == 'POST':
        Form_Registration = Register(request.POST)
        if Form_Registration.is_valid():
            username = Form_Registration.cleaned_data['username']
            password = Form_Registration.cleaned_data['password']
            first_name = Form_Registration.cleaned_data['first_name']
            last_name = Form_Registration.cleaned_data['last_name']
            selected = Form_Registration.cleaned_data.get("choice")

            var = True # if selected == "business" else False
            
            # Get all information from the fields
            u = User.objects.filter(username = username).exists() # checks to see if username is in database
            if u: # IF User is in database, then log in, else redirect to register//make new User object
                error(request,"User is already in database")
                return redirect('/register/')
            else:
                
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = first_name,
                    last_name = last_name,
                    is_staff = var, # False for shoppers,  True for business
                ).save()
                user = authenticate(username = username, password = password)
                userModel = User.objects.get(username = username)
                login(request,userModel)
                return redirect('/' + selected + '/')
            
    context = {
        'form_registration': Form_Registration,
    }        
    return render(request,registerHTML,context)

def business_page(request):
    businessHTML = 'Home/business.html'

    Form_Registration = Business()

    if request.method == 'POST':
        Form_Registration = Business(request.POST)
        if Form_Registration.is_valid():
            description = Form_Registration.cleaned_data['description']
            request.user.update(
                email = description
            )
            return redirect('/')

    context = {
        'form_registration': Form_Registration,
    }        
    return render(request,businessHTML,context)

def shopper_page(request):
    shopperHTML = 'Home/shopper.html'

    Form_Registration = Shopper()

    if request.method == 'POST':
        Form_Registration = Shopper(request.POST)
        if Form_Registration.is_valid():
            description = Form_Registration.cleaned_data['description']
            request.user.update(
                email = description
            )
            return redirect('/')

    context = {
        'form_registration': Form_Registration,
    }        
    return render(request,shopperHTML,context)






