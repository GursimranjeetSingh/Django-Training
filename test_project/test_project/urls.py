from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from api.views import TestViewSet


router=routers.DefaultRouter()
router.register('test',TestViewSet,'This is a test api')
router.register('car',TestViewSet,'This is a test api')


urlpatterns = [
    path("",include(router.urls)),
    path('admin/', admin.site.urls),
]


