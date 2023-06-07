from django.db import models
from django.contrib.auth.models import User
# Dedicado a Catiihidalgo, gracias amor por cada empuje y levante de animo, sin tí no estaría dando este certamen. love u
class Categoria(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Comunicado(models.Model):

    """
    Modelo para representar las categorías de los comunicados.

    - nombre: Campo de texto para el nombre de la categoría.
    - descripcion: Campo de texto para la descripción de la categoría.
    """

    NIVEL_CHOICES = [
        ("GEN", "General"),
        ("PRE", "Ciclo Preescolar"),
        ("BAS", "Ciclo Básico"),
        ("MED", "Ciclo Medio"),
    ]

    correlativo = models.AutoField(primary_key=True)
    titulo = models.TextField()
    detalle = models.TextField()
    nivel = models.CharField(max_length=3, choices=NIVEL_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
