from django.db import models

class User(models.Model):
    USER_TYPE_CHOICES = [
        (1, 'client'),
        (2, 'admin'),
        (3, 'more'),
    ]

    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    type = models.IntegerField(choices= USER_TYPE_CHOICES, default=1)

    def __str__(self):
        return self.name

    
    


