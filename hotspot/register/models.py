from django.db import models

# Create your models here.
class Clients(models.Model):
    email = models.EmailField()
    def __unicode__(self):
        return self.name
