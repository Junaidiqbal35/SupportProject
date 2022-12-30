from django.db import models


# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=23)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.name} contact you.'
