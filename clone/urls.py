from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name='clone'

urlpatterns = [
    path('',views.signin, name='signin'),
    path('instagram/',views.instagram, name='interface'),
    path('login/',views.login, name='login'),
    path('profile',views.profile, name='profile'),
    path('like',views.likes,name='like_image'),
    path('logout',views.logout,name='logout'),
]

