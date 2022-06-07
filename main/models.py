
from operator import mod
from turtle import title
from django.db import models

from django.contrib.auth.models import User

class Profiles(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE,
    related_name='profile')

    region = models.CharField(max_length=1000, choices=(
        ('B','Bishkek'),
        ('O', 'Osh'),
        ('Batken','A' ),
        ('N', 'Naryn'),
        ('D', 'Djalal-Abad'),
        ('T', 'Talas'),
        ('Y', 'Ysuk-kol'),
        ('Ch', 'Chui'),

    ))
    photo = models.ImageField(upload_to='profile_photo',
    null=True, blank=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username
 

# Create your models here.
