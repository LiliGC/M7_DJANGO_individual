from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Professional
from .forms import ClienteForm,ProfessionalForm
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
def clientes(request):

    client=Client.objects.all()

    context = { 

    'clientes': client, 

    } 
    return render(request,'labtienda/clientes.html', context)

@staff_member_required
@login_required
def profesional(request):

    profesional=Professional.objects.all()

    context = { 

    'professionals': profesional, 

    } 
    return render(request,'labtienda/profesional.html', context)


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

@staff_member_required
@login_required
def registro_professional(request):

    form=ProfessionalForm() 

    if request.method == 'POST': 

        form = ProfessionalForm(request.POST)

        if form.is_valid(): 
            profesional=Professional()
            profesional.title=form.cleaned_data["title"]
            profesional.ci=form.cleaned_data["ci"]
            profesional.name=form.cleaned_data["name"]
            profesional.last_name=form.cleaned_data["last_name"]
            profesional.birth_date=form.cleaned_data["birth_date"]
            profesional.phone=form.cleaned_data["phone"]
            profesional.email=form.cleaned_data["email"]
            profesional.address=form.cleaned_data["address"]
            profesional.save()
            messages.success(request, 'Los datos han sido guardados satisfactoriamente') 
            return redirect('profesional') 

        else: messages.error(request,'Inválido') 

        return redirect('registro_profesional') 

    else: 

        form=ProfessionalForm()  

        return render(request, 'labtienda/registro_profesional.html', {"form":form}) 

@login_required
def profesional_edit(request,pk):
    profesional = get_object_or_404(Professional, pk=pk)
    if request.method == "POST":
        form = ProfessionalForm(request.POST, instance=profesional)
        if form.is_valid():
            profesional = form.save(commit=False)
            profesional.save()
            messages.success(request, 'El profesional se ha modificado con éxito')
            return redirect('profesional')
    else:
        form = ProfessionalForm(instance=profesional)
    return render(request, 'labtienda/profesional_edit.html', {'form': form})

@login_required
def profesional_delete(request,pk):
    profesional = get_object_or_404(Professional, pk=pk)
    profesional.delete()
    messages.success(request, 'El profesional se ha eliminado con exito')        
    return redirect('profesional')

@login_required
def cliente_edit(request,pk):
    cliente = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            messages.success(request, 'El cliente se ha modificado con éxito')
            return redirect('usuarios')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'labtienda/cliente_edit.html', {'form': form})

@login_required
def cliente_delete(request,pk):
    cliente = get_object_or_404(Client, pk=pk)
    cliente.delete()
    messages.success(request, 'El cliente se ha eliminado con exito')        
    return redirect('usuarios')


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