from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Casier
from .forms import CasierForm, ConnexionForm


def loginuser(request):
	error = False
	connect = True
	if request.user.is_authenticated():
		return redirect('success')
		print(request.user.is_authenticated())

	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']  
			password = form.cleaned_data['password']  
			user = authenticate(username=username, password=password) 
			if user:  
				login(request, user)
				return redirect('success')
			else: 
				error = True
	else:
		form = ConnexionForm()
	return render(request, 'login.html',locals())


def success(request):
	queryset = Casier.objects.all().filter(user=request.user)
	return render(request, 'success.html', locals(), context_instance=RequestContext(request))



def welcome(request):
	return render(request, 'home.html')

def check(request, id):
	casier = get_object_or_404(Casier, id=id)
	if casier.libre:
		request.session['casier_id'] = id
		return HttpResponseRedirect(reverse(signup))    
	
	else:
		casierfree=Casier.objects.all().filter(libre=True)
		if casierfree:
			totalfail = False
			casierfree=Casier.objects.all().filter(libre=True)[0]
			return render(request, 'fail.html', locals())
		else:
			totalfail = True
			return render(request, 'fail.html', locals())


def signup(request, id):
	casier = get_object_or_404(Casier, id=id)
	if casier.libre:
		if request.method == 'POST':
			form = CasierForm(request.POST)
			if form.is_valid():
				email = form.cleaned_data['email']
				pseudo = form.cleaned_data['pseudo']
				try:
					username = User.objects.get(username = email)
					casier.user = username
				except User.DoesNotExist: 
					Password = User.objects.make_random_password()
					casier.user = User.objects.create_user(username = email,first_name = pseudo,password = Password, email = email)
					casier.save()
				casier.pseudo = pseudo
				casier.objet = form.cleaned_data['objet']
				casier.email = email
				casier.libre = False
				casier.save()

				valide = True
		else:
			form = CasierForm()
		
		return render(request, 'signup.html', locals())

	else:
		casierfree=Casier.objects.all().filter(libre=True)
		if casierfree:
			totalfail = False
			casierfree=Casier.objects.all().filter(libre=True)[0]
			return render(request, 'fail.html', locals())
		else:
			totalfail = True
			return render(request, 'fail.html', locals())










