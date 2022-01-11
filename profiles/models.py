from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_mob_number = models.CharField(max_length=15, null=True, blank=True)
    default_first_address_line = models.CharField(
        max_length=80, null=True, blank=True)
    default_second_address_line = models.CharField(
        max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=30, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=15, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user(sender, instance, created, **kwargs):
    """
    Create or update userprofiles
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
