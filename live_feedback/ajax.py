import json
from dajaxice.decorators import dajaxice_register

# from live_feedback.models import Event


@dajaxice_register
def sayhello(request):
  return json.dumps({'message':'Hello World'})
