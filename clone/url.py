from django.conf import settings
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('instagram',views.instagram, name='interface')
]