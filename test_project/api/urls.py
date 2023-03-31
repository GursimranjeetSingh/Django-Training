from .views import *
from rest_framework import routers
router=routers.DefaultRouter()

router.register('bike',BikeViewSet,'This is a test api')
router.register('car',BikeViewSet,'This is a test api')
