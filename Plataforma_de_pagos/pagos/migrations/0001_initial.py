# Generated by Django 2.2.12 on 2022-06-04 23:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idtransaccion', models.CharField(max_length=50)),
                ('nombre', models.CharField(help_text='Nombre y Apellido', max_length=30)),
                ('email', models.CharField(help_text='Correo', max_length=30)),
                ('idcomprador', models.CharField(help_text='Identificador del comprador', max_length=30)),
                ('conpago', models.CharField(help_text='Concepto de pago', max_length=30)),
                ('sede', models.CharField(help_text='sede', max_length=30)),
                ('franquicia', models.CharField(help_text='Franquicia', max_length=30)),
                ('monto', models.IntegerField(help_text='Monto a pagar', validators=[django.core.validators.MinValueValidator(1)])),
                ('debito', models.BooleanField(default=False)),
                ('tarjeta', models.CharField(max_length=30)),
                ('cuotas', models.IntegerField(default=1, help_text='Numero de cuotas')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjetas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(help_text='Elija un banco', max_length=50)),
                ('tipo', models.CharField(help_text='Tipo de tarjeta', max_length=16)),
                ('nombre', models.CharField(help_text='Propietario', max_length=20)),
                ('numero', models.CharField(help_text='1111 2222 3333 4444', max_length=19, unique=True)),
                ('cvv', models.CharField(help_text='CVV', max_length=4)),
                ('vencimiento', models.CharField(help_text='08/22', max_length=5)),
                ('estado', models.BooleanField(default=True)),
                ('saldo', models.IntegerField(default=1000000)),
                ('tipodocumento', models.CharField(help_text='tipo de documento', max_length=50)),
                ('numeroid', models.CharField(help_text='Numero identidad', max_length=50)),
                ('email', models.CharField(help_text='Email', max_length=50)),
                ('tipopersona', models.CharField(help_text='Tipo de persona', max_length=50)),
                ('credito', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]