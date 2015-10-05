from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True)
    profile_image = models.ImageField(upload_to = 'static/', default = 'static/default.jpg')

    def __unicode__(self):
        return self.user.username
