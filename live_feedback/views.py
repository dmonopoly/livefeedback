from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render, render_to_response

def index(request):
  context = {
    'x': 6.8
  }
  return render(request, 'live_feedback/index.html', context)

def vote(request):
  context = {

  }
  return render(request, 'live_feedback/vote.html', context)
