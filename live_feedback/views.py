from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render, render_to_response

def index(request):
  latest_poll_list = range(9)
  context = {
    'x': latest_poll_list,
  }
  return render(request, 'live_feedback/index.html', context)

def vote(request):
  context = {

  }
  return render(request, 'live_feedback/vote.html', context)
