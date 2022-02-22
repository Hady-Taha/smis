from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Professor


@receiver(post_save, sender=User)
def post_save_create_profile(created, sender, instance, *args, **kwargs):
    if created:
        Professor.objects.create(user=instance)
