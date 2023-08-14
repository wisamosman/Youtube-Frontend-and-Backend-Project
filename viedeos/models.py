from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    

class Video(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='viedeos')
    author = models.ForeignKey(Author,related_name='video_author',on_delete=models.CASCADE)
    description = models.TextField(max_length=30000)
    likes = models.ManyToManyField(User, related_name='video_like')
    dislikes = models.ManyToManyField(User,related_name='video_dislikes')
    tags = TaggableManager()
    video = models.CharField(max_length=200 , blank=True , null=True)
    

    def __str__(self):
        return self.name




class Review(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    comments = models.ForeignKey(Video,related_name='comments_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(max_length=500)
    
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} = {self.comments}"