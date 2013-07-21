#-*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from mechofduty.gamer.forms import GamerCreationForm

def register(request):
  if request.method == "POST":
    form_register = GamerCreationForm(request.POST)
    if form_register.is_valid():
      user = form_register.save()
      redirect('register_creategamer', user_id=user.pk)
  else:
    form_register = GamerCreationForm()
  return render_to_response('gamer/register.html', {'form_register': form_register,
                                                      },context_instance=RequestContext(request))

def register_gamer(request, user_id):
    return 'OK'