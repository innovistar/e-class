from django.db import models

#from embed_video.fields import EmbedVideoField

from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    note = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.course
        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except :
            url = ''
        return url

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.CharField(max_length=200)
    #video_url = EmbedVideoField()
    other_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.topic
