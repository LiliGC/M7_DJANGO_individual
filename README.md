# M7 AE2 individual

**Liliana Garmendia**

Este proyecto es una continuación de M7 AE1 individual que está en esta cuenta, en esta oportunidad se ha incluido los comentarios al sitio web mediante un formulario de contacto con opciones de mensaje de consulta, felicitación, sugerencia o reclamo. Se puede acceder sin estar registrado mediante el enlace en la barra de navegación Contáctanos. Si ha iniciado sesión tiene acceso a ver la lista de comentarios y puede acceder a editar o eliminar los que haya enviado. Se pusó la restricción en la views de @login_required y en el template de acceso a editar o eliminar si el usuario que ha iniciado sesión es el mismo que creó el comentario le aparecerán los botones para editar o eliminar. 

Además se agregó el CRUD para los clientes y profesionales, por lo que cada uno cuenta con formulario de registro, edición, eliminación y ver el listado con datatable con las opciones de descargar un pdf en los botones de las tablas. Desde el sitio web para acceder a modificar o eliminar éstos necesita ser parte del staff, por lo que en las views se agregó la restricción  @staff_required.

Se cambió también la base de datos a Mysql, y se modificó el admin de django con django interface.

## Instrucciones para instalación

## Instalación

-Clonar el repositorio usando gitbash o el terminal que tenga en su computador local con el siguiente comando:

``` git clone https://github.com/LiliGC/M7_DJANGO_individual.git ```
-Abrir la carpeta con el repositorio clonado en un editor de texto como Visual Studio Code con la opción indicada en la imagen.
![vscode](labtienda/static/img/visualcode.png)
-Abrir un nuevo terminal en Visual Studio Code y crear el entorno virtual con el siguiente comando:
```pip install venv venv ```
-Luego activar el entorno virtual:
```cd venv/Scripts/activate ```
-Volver a la carpeta principal con cd ..
-Ahora instalar requirements con el siguiente comando:
```pip install -r requirements.txt```
-Hacer las migraciones con el comando:
``` python manage.py migrate```
-Crear tu superusuario para acceder al admin:
```python manage.py createsuperuser```
-Y finalmente levantar el servidor con:
``` python manage.py runserver```

**Observaciones:** Si quisieras cargar los datos que utilicé de prueba tendrías que poner: ```python manage.py loaddata data.json```  y luego correr el comando ``` python manage.py migrate```
Si tienes problemas para cargar los datos por contenttypes debes usar los siguientes comandos ```python manage.py shell``` para acceder a la shell, luego ingresar los siguientes comandos en orden from ```django.contrib.contenttypes.models import ContentType```,  ```ContentType.objects.all().delete()```, ```quit()```. Y luego volver a correr ```python manage.py loaddata data.json```.

## Librerias usadas
Revisar el archivo requirements.txt. Algunas observaciones:
* Se usó la versión más reciente de Django para crear la aplicación.
* Se usó HTML, Bootstrap 5, CSS, JavaScript para crear los templates.
* Para el formulario se usó los que trae django junto con crispy forms para el estilo.
* Para las tablas con el listado de clientes se uso DataTable de jquery.
* Para los mensajes de alerta se usó la librería de sweetalert2.
* Se modificó la página del admin importando la librería admin_interface.