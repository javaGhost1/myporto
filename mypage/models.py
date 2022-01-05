from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=300)
    decription = models.TextField()
    

    def __str__(self):
        return self.name

class Software(models.Model):
    title = models.CharField( max_length=50, primary_key=True)
    desc = models.CharField(max_length=100)
    urls = models.CharField( max_length=100)
    

    class Meta:
        db_table = "spiderCollection1"

    def __str__(self):
        return self.title

    

