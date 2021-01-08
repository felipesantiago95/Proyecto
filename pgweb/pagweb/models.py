from django.db import models

# Create your models here.

class Persona(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(blank=True,max_length=50, verbose_name='nombre')
    apellidos=models.CharField(blank=True,max_length=200, verbose_name='Apellido')
    edad=models.IntegerField()
    telefono=models.CharField(blank=True,max_length=12, verbose_name='Telefono')


class obra(models.Model):
    id=models.AutoField(primary_key=True) 
    cod_work_sq=models.IntegerField() 
    ISWC=models.CharField(blank=True,max_length=10, verbose_name='ISWC')
    titulo=models.CharField(blank=True,max_length=250, verbose_name='Titulo')
    autor=models.CharField(blank=True,max_length=250, verbose_name='Autor')
    persona= models.ForeignKey(Persona, on_delete = models.CASCADE)
