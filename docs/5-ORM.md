1. Definir un modelo

En models.py de una aplicación de Django:

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

Luego, aplica las migraciones:

python manage.py makemigrations
python manage.py migrate

2. Crear registros

Desde el shell de Django (python manage.py shell):

from inventario.models import Producto

producto = Producto(nombre="Teclado", precio=50.00, stock=20)
producto.save()

O usando create():

Producto.objects.create(nombre="Mouse", precio=30.00, stock=15)

3. Consultar registros

Obtener todos los objetos

productos = Producto.objects.all()

Producto.objects.filter(precio__gte=100)  # Productos con precio mayor o igual a 100
Producto.objects.get(id=1)  # Obtener un único objeto por ID

⚠️ get() lanza un error si el objeto no existe o si hay múltiples coincidencias.

Ordenar resultados

Producto.objects.order_by("-precio")  # Orden descendente por precio

Limitar resultados

Producto.objects.all()[:5]  # Solo los primeros 5 registros

4. Actualizar registros

producto = Producto.objects.get(id=1)
producto.precio = 45.00
producto.save()

O con update():

Producto.objects.filter(id=1).update(precio=45.00)

5. Eliminar registros

producto = Producto.objects.get(id=1)
producto.delete()

O con delete() en una consulta:

Producto.objects.filter(precio__lt=20).delete()  # Elimina productos con precio menor a 20

6. Relaciones entre modelos

Si tienes modelos con relaciones:

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

Consultas con relaciones:

Producto.objects.filter(categoria__nombre="Electrónica")