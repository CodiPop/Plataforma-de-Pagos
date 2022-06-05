from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator
# Create your models here.
class Tarjetas(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    banco  = models.CharField(max_length=50, help_text="Elija un banco")
    tipo = models.CharField(max_length=16, help_text="Tipo de tarjeta")
    nombre = models.CharField(max_length=20, help_text="Propietario")
    numero = models.CharField( max_length=19, unique=True, help_text="1111 2222 3333 4444")
    cvv = models.CharField(max_length=4, help_text="CVV")
    vencimiento = models.CharField(max_length=5, help_text="08/22")
    estado = models.BooleanField(default=True)
    saldo = models.IntegerField(default = 1000000)
    tipodocumento = models.CharField(max_length=50, help_text="tipo de documento")
    numeroid = models.CharField(max_length=50, help_text="Numero identidad")
    email =  models.CharField(max_length=50, help_text="Email")
    tipopersona = models.CharField(max_length=50, help_text="Tipo de persona")
    credito = models.BooleanField(default=False)
    def __str__(self):
        return self.numero

class Transacciones(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    idtransaccion = models.CharField(max_length=50)
    nombre = models.CharField(max_length=30, help_text="Nombre y Apellido")
    email = models.CharField(max_length=30, help_text="Correo")
    idcomprador = models.CharField(max_length=30, help_text="Identificador del comprador")
    conpago = models.CharField(max_length=30, help_text="Concepto de pago")
    sede = models.CharField(max_length=30, help_text="sede")
    franquicia = models.CharField(max_length=30, help_text="Franquicia")
    monto = models.IntegerField(help_text="Monto a pagar", validators=[MinValueValidator(1)])
    debito = models.BooleanField(default=False)
    tarjeta =  models.CharField(max_length=30)
    cuotas = models.IntegerField(help_text="Numero de cuotas", default=1)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.nombre}"
    