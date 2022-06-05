from dataclasses import field
from pickle import TRUE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


tipoBanco =(
    ("East Bank", "East Bank"),
    ("Wester Bank", "Wester Bank")
)
tipodocumento = (
    ("C.C.", "C.C."),
    ("C.E.", "C.E."),
    ("NIT", "NIT"),
    ("Otro", "Otro")

)
tipoBanco2 = (
    ("Banco Agrario", "Banco Agrario"),
    ("Banco AV Villas", "Banco AV Villas"),
    ("Banco Caja Social", "Banco Caja Social"),
    ("Banco Davivienda", "Banco Davivienda"),
    ("Banco de Bogota","Banco de Bogota"),
    ("Banco de Occidente", "Banco de Occidente"),
    ("Banco Falabella", "Banco Falabella"),
    ("Banco Popular", "Banco Popular"),
    ("Bancolombia", "Bancolombia"),
    ("Citibank", "Citibank"),
    ("Scotiabank Colpatria", "Scotiabank Colpatria"),
    ("Daviplata", "Daviplata"),
    ("Rappipay", "Rappipay"),
)
tipopersona =(
    ('Natural','Natural'),
    ('Juridica','Juridica')
)
tipoTarjeta=(
    ('Visa','Visa'),
    ('Mastercard','Mastercard'),
    ('Amex','American Express')
)


class transForm(forms.ModelForm):
    class Meta:
        model = Transacciones
        fields = [
            'nombre', 'email','idcomprador','conpago', 'sede', 'franquicia',
            'monto', 'debito', 'tarjeta', 'cuotas'
            ]
    def __init__(self, author, *args, **kwargs): 
        super(transForm, self).__init__(*args, **kwargs) 
        self.fields['tarjeta'] = forms.ModelChoiceField(queryset=Tarjetas.objects.filter(author=author))
        
class PSE(forms.ModelForm):
    tipodocumento = forms.ChoiceField(choices=tipodocumento)
    tipopersona = forms.ChoiceField(choices=tipopersona)
    banco = forms.ChoiceField(choices=tipoBanco2)
    tipo = forms.ChoiceField(choices=tipoTarjeta)
    class Meta:
        model = Tarjetas
        fields = ['tipodocumento', 'numeroid', 'tipopersona','banco', 'email','tipo','nombre', 'numero','cvv','vencimiento', 'estado']
        

class cardForm(forms.ModelForm):
    banco = forms.ChoiceField(choices=tipoBanco)
    tipo = forms.ChoiceField(choices=tipoTarjeta)
    class Meta:
        model = Tarjetas
        fields = ['banco', 'tipo','nombre', 'numero','cvv','vencimiento', 'estado']
        

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields }
