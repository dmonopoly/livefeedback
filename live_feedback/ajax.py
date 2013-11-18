import json
from dajaxice.decorators import dajaxice_register

from live_feedback.models import Event

STEP = .5
# These values should correspond to those in range of gauge set in index.html:
NEUTRAL = 5
MIN = 0
MAX = 10


@dajaxice_register
def increment(request):
  e = Event.objects.all()[0]
  if e.mood < MAX:
    e.mood += STEP
    e.save()
  return json.dumps({'mood': e.mood})

@dajaxice_register
def decrement(request):
  e = Event.objects.all()[0]
  if e.mood > MIN:
    e.mood -= STEP
    e.save()
  return json.dumps({'mood': e.mood})

@dajaxice_register
def checkToUpdateReading(request):
  e = Event.objects.all()[0]
  return json.dumps({'mood': e.mood})

# @dajaxice_register
# def neutralizeByOneStep(request):
#   e = Event.objects.all()[0]
#   if e.mood < NEUTRAL:
#     e.mood += STEP
#   elif e.mood > NEUTRAL:
#     e.mood -= STEP
#   e.save()
#   return json.dumps({'mood': e.mood})
