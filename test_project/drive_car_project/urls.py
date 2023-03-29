from rest_framework.routers import SimpleRouter

from .views import *


router=SimpleRouter()

router.register('car',CarViewSet)
router.register('driver',DriverViewSet)