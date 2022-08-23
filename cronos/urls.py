from django.urls import path


from cronos import views
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register(r"jobs", views.JobViewSet, basename="Job")


urlpatterns = [path("", include(router.urls))]
