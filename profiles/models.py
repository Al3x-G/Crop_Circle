from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    UserProfile model to store and manage additional user information:
    - Keeps track of delivery details (phone, address) and order history.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Stores the user's default phone number.
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)  # noqa: E501 (Fix flake 8 line too long)

    # Stores the first line of the user's default street address.
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)  # noqa: E501 (Fix flake 8 line too long)

    # Stores the second line of the user's default street address.
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)  # noqa: E501 (Fix flake 8 line too long)

    # Stores the user's default town or city.
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)  # noqa: E501 (Fix flake 8 line too long)

    # Stores the user's default county, nullable and blank fields allowed
    default_county = models.CharField(max_length=80, null=True, blank=True)

    # Stores the user's default postcode.
    default_postcode = models.CharField(max_length=20, null=True, blank=True)

    # A country field with a blank label.
    default_country = CountryField(blank_label='Country', null=True, blank=True)  # noqa: E501 (Fix flake 8 line too long)

    def __str__(self):
        # Returns the username associated with this user profile
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler creates/updates the UserProfile when User model is saved.
    - Creates a UserProfile when a new user is created.
    - Updates the profile if the user already exists.
    """
    if created:
        # Creates a UserProfile instance for the newly created user
        UserProfile.objects.create(user=instance)
    # For existing users, the profile is saved (updated if necessary)
    instance.userprofile.save()
