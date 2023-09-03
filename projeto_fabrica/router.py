from rest_framework import routers
from vehicleshop.views import CarroViewset, MotoViewset

router = routers.DefaultRouter()
router.register(r'carro', CarroViewset)
router.register(r'moto', MotoViewset)
urlpatterns = router.urls