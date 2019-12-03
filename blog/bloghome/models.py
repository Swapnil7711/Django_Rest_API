from django.db import models

# Create your models here.

class AppUsers(models.Model):

    username = models.CharField(max_length = 20, unique = True)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)


    def __str__(self):

        return self.firstname


