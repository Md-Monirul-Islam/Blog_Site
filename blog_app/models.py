from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    post_date = models.DateField(default=date.today)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name + '==>' + str(self.author)

    def save(self, *args, **kwargs):
        if not self.id:  # Check if the object is being created for the first time
            self.slug = slugify(self.name + "-" + str(self.post_date))
        super().save(*args, **kwargs)
        

class BlogComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    comment_date = models.DateField(auto_now_add=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog)