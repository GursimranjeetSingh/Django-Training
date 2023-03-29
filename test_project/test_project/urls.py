from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from api.views import *
from drive_car_project.urls import router as drive_car_router


router=routers.DefaultRouter()

router.register('bike',BikeViewSet,'This is a test api')

urlpatterns = [
    path("",include(router.urls)),
    path("drive_car_project/",include(drive_car_router.urls)),
    path('admin/', admin.site.urls),
]


