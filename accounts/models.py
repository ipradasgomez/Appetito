from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from plans.models import Plan
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, default=1, on_delete=models.SET_DEFAULT)

def plan_or_default(self):
    return self.plan or Plan.objects.get().first()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("Trying to create Profile", "User:", instance.id, "Plan:", Plan.objects.all().first().id)
    if created:
        Profile.objects.create(user_id=instance.id, plan_id=Plan.objects.all().first().id)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
