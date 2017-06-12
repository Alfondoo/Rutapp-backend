from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from rutas.views import RutasViewSet

router = routers.DefaultRouter()
router.register(r'rutas', RutasViewSet, base_name="rutas")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
