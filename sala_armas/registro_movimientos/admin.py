from django.contrib import admin
from .models import User, Armamento, Usuario, Movimiento

# Register your models here.
class ArmamentoAdmin(admin.ModelAdmin):
    list_filter =("tipo", "ni")
    list_display =("tipo", "ni")

class MovimientoAdmin(admin.ModelAdmin):
    list_filter = ("fechahora", "tipo", "usuario", "armamento", "motivo")
    list_display =("fechahora", "tipo", "usuario", "armamento", "motivo")
    
class UsuarioAdmin(admin.ModelAdmin):
    list_filter = ('grado', 'nombre', 'apellido', 'dni', 'rol', 'subun')
    list_display = ('grado', 'nombre', 'apellido', 'dni', 'rol', 'subun')

admin.site.register(Armamento, ArmamentoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Movimiento, MovimientoAdmin)
