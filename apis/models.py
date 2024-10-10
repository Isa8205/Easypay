from django.db import models

# Create your models here.
class Somebody(models.Model):
    firstname = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=False)
    age = models.IntegerField
    birthdate = models.DateField
    profile = models.FileField(upload_to='profiles', null=True)
    phone = models.IntegerField

    def __str__(self):
        return self.firstname