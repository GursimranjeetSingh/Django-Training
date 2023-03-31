from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from api.views import *
from drive_car_project.urls import router as drive_car_router
from api.urls import router as api_router


urlpatterns = [
    path("",include(api_router.urls)),
    path("drive_car_project/",include(drive_car_router.urls)),
    path('admin/', admin.site.urls),
]


