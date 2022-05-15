from django.contrib import admin
from .models import Client, Professional, Comentario

# Register your models here.

admin.site.register(Client)
admin.site.register(Professional)
admin.site.register(Comentario)