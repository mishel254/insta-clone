from django.contrib import admin
from .models import Users,Bio,Post,like,Profiles

# Register your models here.
admin.site.register(Users)
admin.site.register(Bio)
admin.site.register(Post)
admin.site.register(like)
admin.site.register(Profiles)

