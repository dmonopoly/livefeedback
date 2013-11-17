import json
from dajaxice.decorators import dajaxice_register

from live_feedback.models import Event

STEP = .5
NEUTRAL = 5  # Depends on range of gauge set in index.html


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

@dajaxice_register
def neutralizeByOneStep(request):
  e = Event.objects.all()[0]
  if e.mood < NEUTRAL:
    e.mood += STEP
  elif e.mood > NEUTRAL:
    e.mood -= STEP
  e.save()
  return json.dumps({'mood': e.mood})

