from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from posts.views import PostModelViewSet



router = routers.DefaultRouter()
router.register("posts", PostModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls))
    
]
