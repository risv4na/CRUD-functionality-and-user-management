from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Director(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class CensorDetail(models.Model):
    rating = models.CharField(max_length=20)
    certified_by = models.CharField(max_length=30)

class Movies(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    summery = models.TextField()
    thumbnail = models.ImageField(upload_to='images', default='images')
    censor_details = models.OneToOneField(CensorDetail, null=True, on_delete=models.SET_NULL, related_name='movie')
    director_name = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL, related_name="director",default="")
    actors = models.ManyToManyField(Actor, related_name="acted_movie", default="no one")
    
    def __str__(self):
        return self.name

