from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone

from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=70)
    date_time = models.DateField('Event date time', default=timezone.now)
    description = models.TextField()
    enabled = models.BooleanField(default=True)

    def __str__(self):           
        return self.name

class Person(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
      
class Attendance(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.person.full_name} is Attending the Event: {self.event.name}"
