import json
from dajaxice.decorators import dajaxice_register

from live_feedback.models import Event

STEP = .5


@dajaxice_register
def increment(request):
  e = Event.objects.all()[0]
  e.mood += STEP
  e.save()
  return json.dumps({'mood': e.mood})


@dajaxice_register
def decrement(request):
  e = Event.objects.all()[0]
  e.mood -= STEP
  e.save()
  return json.dumps({'mood': e.mood})

