from rest_framework.serializers import ModelSerializer
from rutas.models import Ruta, Punto
from datetime import datetime


class PuntoSerializer(ModelSerializer):
    class Meta:
        model = Punto
        exclude = ('ruta',)


class RutasSerializer(ModelSerializer):
    puntos = PuntoSerializer(many=True)

    class Meta:
        model = Ruta
        fields = '__all__'

    def create(self, validated_data):
        if self.is_valid():
            puntos = self.validated_data.pop('puntos')
            ruta = Ruta.objects.create(**self.validated_data)
            for punto in puntos:
                Punto.objects.create(**punto, ruta=ruta)
            return ruta

    def update(self, instance, validated_data):
        if self.is_valid():
            puntos = self.validated_data.pop('puntos')
            instance.update(**validated_data)
            return instance

    def to_representation(self, instance):
        ret = super(RutasSerializer, self).to_representation(instance)
        ret.pop("puntos")
        if instance.created_at:
            ret['created_at'] = instance.created_at.strftime('%d/%m/%Y %H:%M')
        return ret


class RutasDetailSerializer(ModelSerializer):
    puntos = PuntoSerializer(many=True)

    class Meta:
        model = Ruta
        fields = '__all__'
