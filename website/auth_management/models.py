from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
   auther= models.ForeignKey(User,on_delete=models.CASCADE)
   title= models.CharField(max_length=120)
   body=models.TextField()
   post_date= models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.title

