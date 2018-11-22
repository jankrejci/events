from django.db import models

class Event(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 200)
    location = models.CharField(max_length = 500)
    category = models.CharField(max_length = 20)
