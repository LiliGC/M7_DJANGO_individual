from django.shortcuts import render, redirect
from .models import Client
from .forms import ClienteForm
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 

# Create your views here.
def index(request):

    return render(request,'labtienda/index.html')

@staff_member_required
@login_required
def usuarios(request):

    client=Client.objects.all().values() 

    context = { 

    'clientes': client, 

    } 
    return render(request,'labtienda/usuarios.html', context)

@staff_member_required
@login_required
def registro_cliente(request):

    form=ClienteForm() 

    if request.method == 'POST': 

        form = ClienteForm(request.POST)

        if form.is_valid(): 
            cliente=Client()
            cliente.ci=form.cleaned_data["ci"]
            cliente.name=form.cleaned_data["name"]
            cliente.last_name=form.cleaned_data["last_name"]
            cliente.birth_date=form.cleaned_data["birth_date"]
            cliente.phone=form.cleaned_data["phone"]
            cliente.email=form.cleaned_data["email"]
            cliente.address=form.cleaned_data["address"]
            cliente.save()
            messages.success(request, 'Los datos han sido guardados satisfactoriamente') 
            return redirect('registro') 

        else: messages.error(request,'Inválido') 

        return redirect('registro') 

    else: 

        form=ClienteForm()  

        return render(request, 'labtienda/registro.html', {"form":form}) 

def register_user(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect('index')
		messages.error(request, "Registro no exitoso. Información no válida.")
	form = NewUserForm()
	return render (request, 'labtienda/register_user.html', context={"register_form":form})

def login_user(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Tu haz iniciado sesión como {username}.")
				return redirect('index')
			else:
				messages.error(request,"Nombre o contraseña no válidos.")
		else:
			messages.error(request,"Nombre o contraseña no válidos.")
	form = AuthenticationForm()
	return render(request, 'labtienda/login.html',context={"login_form":form})

@login_required
def logout_user(request):
	logout(request)
	messages.info(request, "Haz cerrado sesión exitosamente.") 
	return redirect('index')