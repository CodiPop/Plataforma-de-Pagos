from django.http import HttpRequest
from django.utils.crypto import get_random_string
from django.shortcuts import redirect, render
from .forms import *

# Create your views here.
def inicio(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
       return redirect('login')

def cards(request):
    tarjetas = Tarjetas.objects.filter(author = request.user)
    contexto = {
        'formulario':tarjetas,
        }
    return render(request,'cards.html', contexto)

def transacciones(request):
    transaccion = Transacciones.objects.filter(author = request.user)
    contexto = {
        'formulario':transaccion,
        }
    return render(request,'transacciones.html', contexto)

def registrarse(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('login')
        else:
            print("Formulario no valido")
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request,'register.html', context)


def creartarjeta(request):
    if request.method =='GET':
        form = cardForm()
        contexto = {
        'form':form
        }
    else:
        form = cardForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            
            task = form.save(commit=False)
            task.author= request.user
            task.save()
            form = cardForm()
            return render(request,'registercard.html', {"form":form, "mensaje":'OK'})
    return render(request,'registercard.html', {"form":form})


def creartarjetapse(request):
    if request.method =='GET':
        form = PSE()
        contexto = {
        'form':form
        }
    else:
        form = PSE(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.cleaned_data['tipodocumento']
            form.cleaned_data['tipopersona']
            form.cleaned_data['banco']
            form.cleaned_data['tipo']

            task = form.save(commit=False)
            task.author= request.user
            task.credito = True
            task.save()
            form = PSE()
            return render(request,'pse.html', {"form":form, "mensaje":'OK'})
    return render(request,'pse.html', {"form":form})

def crearpago(request):
    if request.method =='GET':
        form = transForm(author=request.user)
        contexto = {
        'form':form
        }
    else:
        form = transForm(request.user, request.POST)
        contexto = {
        'form':form
        }
        
        
        if form.is_valid():

            form.cleaned_data['tarjeta']
            tarjeta = Tarjetas.objects.filter(id = form.data['tarjeta']).first()
            
            if tarjeta.estado:
                form.cleaned_data['tarjeta']
                if tarjeta.credito :
                    if int(form.data['cuotas']) > 1 :
                        form = transForm(author=request.user)
                        return render(request,'pagos.html', {"form":form, "mensaje":'cuota'})
            
                        
                if int(form.data['monto']) < tarjeta.saldo :
                    tarjeta.saldo = tarjeta.saldo - int(form.data['monto'])
                    print("NUEVO SALDOO",tarjeta.saldo)
                    tarjeta.save()
                    task = form.save(commit=False)
                    task.author = request.user
                    task.idtransaccion = get_random_string(length=32)
                    task.estado = True
                    task.save()
                    form = transForm(author=request.user)
                    return render(request,'pagos.html', {"form":form, "mensaje":'OK'})
                else:
                    task = form.save(commit=False)
                    task.author = request.user
                    task.idtransaccion = get_random_string(length=32)
                    task.estado = False
                    task.save()
                    form = transForm(author=request.user)
                    return render(request,'pagos.html', {"form":form, "mensaje":'fondos insuficientes'})
            else:
                task = form.save(commit=False)
                task.author = request.user
                task.idtransaccion = get_random_string(length=32)
                task.estado = False
                task.save()
                form = transForm(author=request.user)
                return render(request,'pagos.html', {"form":form, "mensaje":'Tarjeta inactiva'})
    return render(request,'pagos.html', {"form":form})


