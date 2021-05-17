from django.shortcuts import render, redirect
from .forms import RegisterForm, AuthenticateLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('login_user')
        messages.error(request, 'Registration unsuccessful. Invalid information.')
    form = RegisterForm
    return render(request=request, template_name='registers/register_forms.html', context={'register_form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticateLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Successfully logged in as {email}.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Invalid email or password')
    form = AuthenticateLoginForm()
    return render(request=request, template_name='registers/login_forms.html', context={'login_form':form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('login_user')