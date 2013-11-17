from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render, render_to_response

from live_feedback.models import Event


def index(request):
  context = {
    'mood_initial': Event.objects.all()[0].mood
  }
  return render(request, 'live_feedback/index.html', context)


def vote(request):
  context = {

  }
  return render(request, 'live_feedback/vote.html', context)
