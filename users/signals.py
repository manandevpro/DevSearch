from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance, created, **kwargs):
    if created:
        newUser = instance
        profile = Profile.objects.create(
            user = newUser,
            username = newUser.username,
            email = newUser.email,
            name =  newUser.first_name,
        )

        subject = 'Welcome to DevSearch!'
        message = 'We are glad you are here...'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email, ],
            fail_silently=False,
        )
post_save.connect(createProfile, sender=User)


@receiver(post_save, sender=Profile)    
def profileUpdated(sender, instance, created, **kwargs):
    print("Profile Updated")
    print('Instance:', instance)
    print('CREATED:', created)
# post_save.connect(profileUpdated, sender=Profile)


def editAccount(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

post_save.connect(editAccount, sender=Profile)


# """ To delete a User when a respective Profile deletes """
#@receiver(post_delete, sender=Profile)   
def profileDelete(sender, instance, **kwargs):
    try:
        userProfile = instance.user
        userProfile.delete()
    except:
        pass

post_delete.connect(profileDelete, sender=Profile)