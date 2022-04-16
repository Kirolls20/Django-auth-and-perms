from django.db.models.signals import post_save
from django.contrib.auth.models import Group,User
from .models import Post

def add_to_default_group(sender,instance, created,**kwargs):
   #user= kwargs['instance']
   if created:
      group,ok = Group.objects.get_or_create(name='default')
      instance.groups.add(group)
      Post.objects.create(
         auther= instance,
         # name=instance.username
      )

post_save.connect(add_to_default_group,sender=User)

