from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

JOB_TYPE = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time")
)



def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)


class Job (models.Model):
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length= 20, choices=JOB_TYPE)
    description = models.TextField(max_length=1500)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        return super().save(*args, **kwargs)

class Category (models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
    
class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applay_job')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    web_site = models.URLField(null=True)
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=700)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name