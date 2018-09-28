
from django.db import models
from django.utils import timezone

class Type(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Record(models.Model):
   
    price = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title
        