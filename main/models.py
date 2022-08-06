from django.db import models

# Create your models here.
class Result(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    result = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
