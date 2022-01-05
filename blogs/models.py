from django.db import models

# Create your models here.
class Blog(models.Model):
    topic = models.CharField(max_length=150)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.topic

# class Entry(models.Model):
#     topic = models.ForeignKey(Blog, on_delete=models.CASCADE)
   

#     class Meta:
#         verbose_name_plural = "entries"

#     def __str__(self):
#         """Return a string represention of the model"""
#         return f"{self.text[:100]}..."




    