from django.db import models
from django.contrib.auth.models import User
from plans.models import Plan
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.OneToOneField(Plan, null=True, on_delete=models.SET_NULL)

@property
def plan_or_default(self):
    return self.plan or 1

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
