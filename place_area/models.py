from django.db import models

# Create your models here.
class Region(models.Model):
    region_name = models.CharField(null = False, blank = False, max_length=100)
    slug = models.SlugField(default="", null=False)

    class Meta():
        ordering = ["region_name"]

    def __str__(self):
        return self.region_name
    

class OuterPostCode(models.Model):
    postcode=models.CharField(max_length=10)
    lat=models.FloatField()
    lon=models.FloatField()

    class Meta():
        ordering = ["postcode"]

    def __str__(self):
        return self.postcode
    
class PostCode(models.Model):
    postcode=models.CharField(max_length=10)
    lat=models.FloatField()
    lon=models.FloatField()

    class Meta():
        ordering = ["postcode"]

    def __str__(self):
        return self.postcode