from user.models import *
from property.models import Property


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=2)
    date_of_birtday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    avatar = CloudinaryField('image', default='placeholder')
    favourites = models.ManyToManyField(Property,
                                        blank=True,
                                        related_name='favourites')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def _create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def _save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
