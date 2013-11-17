from django.db import models

class Event(models.Model):
  mood = models.FloatField()

  def __unicode__(self):
    return self.mood
