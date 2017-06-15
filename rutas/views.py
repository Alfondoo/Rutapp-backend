from rest_framework import viewsets
from rutas.models import Ruta
from rutas.permissions import IsMyDevice
from rutas.serializers import RutasSerializer, RutasDetailSerializer


class RutasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsMyDevice,)

    def get_queryset(self):
        return Ruta.objects.all().filter(device=self.request.query_params.get('device'))

    def get_serializer_class(self):
        if self.request.method == 'GET' and self.action == "retrieve":
            return RutasDetailSerializer
        else:
            return RutasSerializer