from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):  #para mostrar el nombre de la ciudad en el admin
        return self.name

    class Meta: #muestra en plurar las ciudades
        verbose_name_plural = 'cities'