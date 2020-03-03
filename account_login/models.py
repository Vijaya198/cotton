from annoying.fields import AutoOneToOneField
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth import get_user_model
from django.db import models
from allauth.account.models import EmailAddressManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

User = settings.AUTH_USER_MODEL
# Create your models here.

#email_confirmed = models.BooleanField(default=False)
#email_confirmed.contribute_to_class(User, 'email_confirmed')


class LoggedInUser(models.Model):


    user = AutoOneToOneField(User, related_name='logged_in_user', on_delete=models.PROTECT)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    #session_key = models.ForeignKey(Session, on_delete=models.PROTECT)


    def __str__(self):

        return self.user.username




#class Profile(models.Model):
 #   user = AutoOneToOneField(User, related_name='profile', on_delete=models.CASCADE)
  #  email_confirmed = models.BooleanField(default=False)

#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
 #  if created:
   #     Profile.objects.create(user=instance)
    #    instance.profile.save()






