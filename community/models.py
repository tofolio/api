from django.db import models

# Create your models here.
class Communitys(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField('community_photos')

    def __str__(self) -> str:
        return self.name