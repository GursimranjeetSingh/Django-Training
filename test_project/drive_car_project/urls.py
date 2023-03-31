from rest_framework.routers import SimpleRouter,DefaultRouter

from .views import *


router=SimpleRouter()

router.register('car',CarViewSet)
router.register('driver',DriverViewSet)