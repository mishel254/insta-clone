from django.contrib import admin
from django.urls import path,include

app_name='clone'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('clone.urls', namespace='clone')),
   
]
