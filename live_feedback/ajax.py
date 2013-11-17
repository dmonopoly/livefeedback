import json
from dajaxice.decorators import dajaxice_register

from live_feedback.models import Event


@dajaxice_register
def increment(request):
  e = Event.objects.all()[0]
  e.mood += 1
  e.save()
  return json.dumps({'mood': e.mood})


@dajaxice_register
def decrement(request):
  e = Event.objects.all()[0]
  e.mood -= 1
  e.save()
  return json.dumps({'mood': e.mood})

