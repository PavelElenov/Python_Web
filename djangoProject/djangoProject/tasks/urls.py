from django.urls import path

from djangoProject.tasks.views import show

urlpatterns = (
    path('', show),
)
