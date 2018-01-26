# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.utils.timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class transaction(models.Model):
    time = models.DateTimeField(default=django.utils.timezone.now)
    qty = models.FloatField()
    amount = models.FloatField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username + " Rs " + str(self.amount) + " " + str(self.qty) + "L"
    
