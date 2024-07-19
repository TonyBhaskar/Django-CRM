from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AddCustomerForm
from .models import Customer

# Create your views here.
@login_required
def home(request):
    customers = Customer.objects.filter(user=request.user)
    return render(request, 'crm/home.html', {'customers': customers})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password = password)
            if user:
                login(request, user=user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'crm/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Here, save without the commit argument, as it defaults to True
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'crm/signup.html', {'form': form})


#for testing the base template
def base(request):
    return render(request, 'crm/base.html')


def addcustomer(request):
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect('home')
    else:
        form = AddCustomerForm()
    return render(request, 'crm/addcustomer.html', {'form': form})

def updatecustomer(request, pk):
    if request.user.is_authenticated:
        customer_record = get_object_or_404(Customer, id=pk)
        
        if request.method == 'POST':
            form = AddCustomerForm(request.POST, instance=customer_record)
            if form.is_valid():
                form.save()
                return redirect('home')  # Redirect to the home page after successful update
        else:
            form = AddCustomerForm(instance=customer_record)
        
        return render(request, 'crm/updatecustomer.html', {'form': form})
    else:
        return redirect('login')  # Redirect to the login page if the user is not authenticated
    
def delete(request, pk):
    if request.user.is_authenticated:
        customer_record = get_object_or_404(Customer, id=pk)
        if request.method == 'POST':
            customer_record.delete()
            return redirect('home')
        return render(request, 'crm/delete.html', {'record': customer_record})
    else:
        return redirect('login')

