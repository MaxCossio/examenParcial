from django.db import models

# Create your models here.
# Create your models here.
class producto(models.Model):
    descripcionProducto = models.CharField(max_length=50,null=True, blank=True)
    codigoProducto = models.CharField(max_length=15,null=True, blank=True)
    precioventaProducto = models.CharField(max_length=15,null=True, blank=True)
    cantidadProducto = models.CharField(max_length=15,null=True, blank=True)
    tiendarelacionada = models.CharField(max_length=20,null=True,blank=True)

class tienda(models.Model):
    direccionTienda = models.CharField(max_length=50,null=True,blank=True)
    codigoTienda = models.CharField(max_length=20,null=True,blank=True)
    provinciaTienda = models.CharField(max_length=50,null=True, blank=True)
    regionTienda = models.CharField(max_length=50,Null=True,blank=True)
    fechaCreacionTienda = models.DateField(null=True)
    telefonoContactoTienda = models.CharField(max_length=20,null=True, blank=True)