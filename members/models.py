from random import choices
from secrets import choice
from django.db import models

# Create your models here.

EDUCATION_CHOICES = (
    ("SSLC", "SSLC"),
    ("+2", "+2"),
    ("GRADUATION", "GRADUATION"),
    ("PG", "PG"),
    ("DOCTRATE", "DOCTRATE"),
)
PROFESSION_CHOICES = (
    ("TEACHING", "TEACHING"),
    ("IT", "IT"),
    ("GULF", "GULF"),
    ("OTHER", "OTHER"),
)


class Member(models.Model):
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    education = models.CharField(max_length=250, blank=True, null=True,  choices=EDUCATION_CHOICES,  )
    profession = models.CharField(max_length=250, blank=True, null=True,  choices=EDUCATION_CHOICES,  )
    graduated = models.CharField(max_length=250, blank=True, null=True)
    address = models.TextField(max_length=250, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name']