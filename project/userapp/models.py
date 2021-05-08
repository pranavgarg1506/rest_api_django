from django.db import models


class UserDetails(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 100)
    telephone = models.CharField(max_length = 10)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length = 20)

    def __str__ (self):
        return self.name