from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from api.views import TestViewSet,BikeViewSet


router=routers.DefaultRouter()

router.register('bike',BikeViewSet,'This is a test api')


urlpatterns = [
    path("",include(router.urls)),
    path('admin/', admin.site.urls),
]


