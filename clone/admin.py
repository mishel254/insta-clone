from django.contrib import admin
from .models import User,Bio,Post

# Register your models here.
admin.site.register(User)
admin.site.register(Bio)
admin.site.register(Post)

