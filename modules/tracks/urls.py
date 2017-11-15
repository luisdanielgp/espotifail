from .views import TrackViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'tracks', TrackViewSet, base_name="tracksViewset")
# DefaultRouter se encarga de crear las rutas a partir de la vista

urlpatterns = router.urls
