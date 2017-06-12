from rest_framework import viewsets
from rutas.models import Ruta
from rutas.permissions import IsMyDevice
from rutas.serializers import RutasSerializer


class RutasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsMyDevice,)
    serializer_class = RutasSerializer

    def get_queryset(self):
        return Ruta.objects.all().filter(device=self.request.query_params.get('device'))
