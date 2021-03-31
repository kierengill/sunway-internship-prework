from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .forms import CreateUserForm
from .decorators import *


def logoutUser(request):
	logout(request)
	return redirect ('/login')

@unauthenticated_user
def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password = password)

		if user is not None:
			login(request, user)
			return redirect ('/products')

		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('/login')


	context = {'form':form}
	return render(request, 'accounts/register.html', context)

@login_required(login_url = 'login')
def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products': products})

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def createProduct(request):
	if request.method == "POST":
		data = request.POST
		image = request.FILES.get('image')
		pdf = request.FILES.get('pdf')

		product = Product.objects.create(
			name = data['name'],
			description = data['description'],
			image = image,
			pdf = pdf,
		)

		return redirect('/products')

	return render(request, 'accounts/product_form.html')

def product_no_login(request):
	products = Product.objects.all()
	return render(request, 'accounts/product_no_login.html', {'products': products})
