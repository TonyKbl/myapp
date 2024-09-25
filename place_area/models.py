from django.db import models

# Create your models here.
class Region(models.Model):
    region_name = models.CharField(null = False, blank = False, max_length=100)
    slug = models.SlugField(default="", null=False)

    class Meta():
        ordering = ["region_name"]

    def __str__(self):
        return self.region_name