from django.shortcuts import redirect, render
from .forms import UserRegisterForm

# Create your views here.
def inicio(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
       return redirect('login')

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
    return render(request,'pages-sign-up.html', context)