from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
      title = models.CharField(max_length=100)
      description = models.TextField()
      organizer = models.CharField(max_length=100)
      date = models.DateField()  
    
    
