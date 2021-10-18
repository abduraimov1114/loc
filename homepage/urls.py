from django.urls import path
from django.urls import path
from .views import HomePageView, AboutPageView, BasePageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('',HomePageView.as_view(), name='home'),
    path('base/', BasePageView.as_view(), name='base' )
]