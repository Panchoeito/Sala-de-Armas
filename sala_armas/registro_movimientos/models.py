from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grado = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    rol = models.CharField(max_length=50)
    subun = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.grado} {self.apellido}"
    
class Armamento(models.Model):
    tipo =  models.CharField(max_length=50)
    ni = models.IntegerField()
    
    def __str__(self):
        return f"{self.tipo} {self.ni}"
    
class Movimiento(models.Model):
    fechahora = models.DateTimeField(auto_now_add=True, blank=True)
    tipo = models.CharField(max_length=50)
    usuario = models.ForeignKey("Usuario", verbose_name=("usuario"), on_delete=models.DO_NOTHING)
    armamento = models.ForeignKey("Armamento", verbose_name=("armamento"), on_delete=models.DO_NOTHING)
    motivo = models.CharField(max_length=50)
    mantenimiento = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return f"{self.tipo}"