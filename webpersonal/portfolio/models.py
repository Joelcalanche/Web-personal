from django.db import models

# Create your models here.
# cada atributo de esta clase sera una columna
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulo")
    description = models.TextField(verbose_name="descripcion")
    
    image = models.ImageField(verbose_name="imagen", upload_to="projets")
    link = models.URLField(verbose_name="direccion web", null=True, blank=True)
    
    # fecha de creacion
    # "auto_now_add, a;ade la hora automaticamente cuando se crea"
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    # fecha de modificacion
    # autonow se ejecuta cada vez que se actualiza una instancia
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        
        return self.title