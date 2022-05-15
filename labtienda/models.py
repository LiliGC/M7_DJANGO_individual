from django.db import models
import datetime



# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=25, verbose_name='Nombre')
    last_name=models.CharField(max_length=25, verbose_name='Apellido')
    birth_date=models.DateField(verbose_name='Fecha de nacimiento', help_text = "Usa el siguiente formato: <em>YYYY-MM-DD</em>.")
    phone=models.IntegerField(verbose_name='Teléfono')
    email=models.EmailField(max_length=254,unique=True, verbose_name='Email')
    address=models.CharField(max_length=100, verbose_name='Dirección', help_text = "Usa el siguiente formato: <em>Calle,número,Población,Comuna</em>.")

    class Meta:
        abstract:True

    def __str__(self):
        return '%s %s'% (self.name, self.last_name)

class Client(User):
    ci=models.CharField(max_length=10, unique=True, verbose_name= 'Run o Rut', help_text = "Usa el siguiente formato: <em>xxxxxxxx-x o xxxxxxxx-x</em>.")
    
class Professional(User):
    title=models.CharField(max_length=50,verbose_name= 'Título')
    ci=models.CharField(max_length=10, unique=True, verbose_name= 'Run')
    registration_date=models.DateField(default=datetime.date.today, verbose_name= 'Fecha de registro')
    

consultas=[
    [0, 'consulta'],
    [1, 'reclamo'],
    [2, 'sugerencia'],
    [3, 'felicitaciones']
]

class Comentario(models.Model):
    nombre= models.CharField(max_length=30)
    correo_electronico=models.EmailField(max_length=30)
    tipo_consulta=models.IntegerField(choices=consultas)
    mensaje=models.TextField()

    def __str__(self): 
        return self.nombre




