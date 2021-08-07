from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet) # Como en la vista se usa el queryset evita el uso de basename

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]