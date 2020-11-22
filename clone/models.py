from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here)
    

class Bio(models.Model):
    city = models.CharField(max_length=30)
    aboutme = models.CharField(max_length=255) 


class User(models.Model):
    username = models.CharField(max_length=30)
    password=models.CharField(max_length=30,default='***')
    email =models.EmailField(default='abc@gmail.com')
    display_photo = CloudinaryField('image')
    followers = models.CharField(max_length=255)
    following = models.CharField(max_length=255)
    bio = models.ForeignKey(Bio,on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    def save_user(self):
        self.save()

    class Meta:
        ordering=['username']

class Post(models.Model):
    photo = CloudinaryField('image')
    caption = models.CharField(max_length=255)

