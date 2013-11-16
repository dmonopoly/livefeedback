from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render, render_to_response

def index(request):
  latest_poll_list = [1,2,3]
  template = loader.get_template('live_feedback/index.html')
  context = RequestContext(request, {
    'x': latest_poll_list,
  })
  return HttpResponse(template.render(context))
#   my_list = [1,2,3]
#   context = {'x': my_list}
#   return render(request, 'live_feedback/index.html', context)

#   return HttpResponse("whatsup");

def home(request):
    return render_to_response('index.html')