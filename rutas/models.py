from django.db import models
from django.db.models import CharField, DateField, FloatField, ForeignKey, DateTimeField


class Ruta(models.Model):
    name = CharField(max_length=64)
    description = CharField(max_length=256)
    created_at = DateTimeField(auto_now_add=True)
    device = CharField(max_length=15)


class Punto(models.Model):
    lat = FloatField()
    long = FloatField()
    height = FloatField()
    ruta = ForeignKey(Ruta, related_name="puntos")
