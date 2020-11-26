from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here)
    

class Bio(models.Model):
    city = models.CharField(max_length=30)
    aboutme = models.CharField(max_length=255) 
    username=models.CharField(max_length=255)

    def __str__(self):
        return self.username

    class Meta:
        ordering=['username']


class Users(models.Model):
    name=models.CharField(max_length=255)
    email =models.EmailField()
    display_photo = CloudinaryField('image',default="url_for('image.jpg')")
    followers = models.CharField(max_length=255,default=0)
    following = models.CharField(max_length=255,default=0)
    bio = models.OneToOneField(Bio,on_delete=models.CASCADE)

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    

def user_deleted():
    return Users.objects.get(post = 'deleted')

class Post(models.Model):
    photo = CloudinaryField('image')
    caption = models.CharField(max_length=255)
    username=models.ForeignKey(Bio,max_length=255,on_delete=models.CASCADE)
    likes =models.ManyToManyField(Users,related_name='imagepost_like')

    def like(self):
        return self.likes
    


