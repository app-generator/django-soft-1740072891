# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    231321 = models.CharField(max_length=255, null=True, blank=True)
    23132131 = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class 123(models.Model):

    #__123_FIELDS__
    52 = models.CharField(max_length=255, null=True, blank=True)
    85 = models.BooleanField()

    #__123_FIELDS__END

    class Meta:
        verbose_name        = _("123")
        verbose_name_plural = _("123")


class 98986(models.Model):

    #__98986_FIELDS__
    231 = models.TextField(max_length=255, null=True, blank=True)
    95621 = models.DateTimeField(blank=True, null=True, default=timezone.now)
    321645654 = models.CharField(max_length=255, null=True, blank=True)

    #__98986_FIELDS__END

    class Meta:
        verbose_name        = _("98986")
        verbose_name_plural = _("98986")



#__MODELS__END
