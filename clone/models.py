from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

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
    likes =models.ManyToManyField(User,related_name='imagepost_like')
    
     
    def __str__(self):
        return str(self.caption)


    @property
    def number_of_like(self):
        return self.likes.count()
LIKE_CHOICES=(
    ('like','like'),
    ('unlike','unlike'),
)
class like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

    def __str__(self):
        return(str(self.post))

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.ForeignKey(Bio,on_delete=models.CASCADE)  
    created = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User, related_name='followers',blank=True)
     
    def get_followers(self):
        return self.followers,all()

    def total_followers(self):
        return self.followers.all().count()

    def __str__(self):
        return str(self.user)

STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted'),
)
class Relationship(models.Model):
    sender = models.ForeignKey(Profiles,on_delete=models.CASCADE,related_name='sender')
    reciever = models.ForeignKey(Profiles,on_delete=models.CASCADE,related_name='reciever')
    created = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=8,choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.sender} - {self.reciever} -{self.status}"
