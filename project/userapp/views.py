from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from rest_framework import viewsets


from .forms import NewUserForm, LoginUserForm
from .serializers import UserSerializer
from .models import UserDetails


# Create your views here.

def register_request(request):
    print("method in registration", request.method)

    ## adding fallback logic
    if request.session.get('username') != None:
        return redirect('/user/')
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print("request.post", request.POST)
        if form.is_valid():
            user_obj = UserDetails(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                telephone = form.cleaned_data['contact'],
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            user_obj.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/user/login')
             ## redirect full path as per the website and it again goes to check urls.py
    else:
        form = NewUserForm()
    return render(request, 'userapp/register.html', {'form': form, 'request':request})


def login_request(request):
    print("Method in login is", request.method)

    ## adding fallback logic
    if request.session.get('username') != None:
        return redirect('/user/')

    if request.session.get('username') == None:
        request.session['username'] = None

    if request.method == 'POST':
        print("Data in request.POST is", request.headers)
        form = LoginUserForm(request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            ## checking athe authentication of credentials
            #user = authenticate(username = username, password = str(password))
            print(username, password)
            rs = UserDetails.objects.filter(username = username)
            print("value of rs is ",rs)
            if len(rs) == 1:
            
                for r in rs:
                    db_password = r.password
                if db_password == password:
                    print("loggin in")
                    request.session['username'] = username

                    return redirect('/user') ## helps  in changing url too at run time
            
                else:
                    print("password is wrong")
                    messages.error(request, 'Invalid Usrname/Password')
            else:
                print("value of the resultset is more than 1")
        else:
            print("Form is corrupted")


    form = AuthenticationForm()
    return render(request=request, template_name="userapp/login.html", context={"form":form, "request":request})


def home_request(request):
    print("method in home_request is", request.method)
    print(request.POST)
    if request.session.get('username') == None:
        request.session['username'] = None
    for key, val in request.session.items():
        print(key, val)
    return render(request, 'userapp/home.html', {'request': request})

def logout_request(request):
    print("method in logout_request is", request.method)
    logout(request)
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    for key, val in request.session.items():
        print(key, val)
    messages.info(request, "You have successfully logged out.") 
    return redirect('/user')

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all().order_by('id')
    serializer_class = UserSerializer