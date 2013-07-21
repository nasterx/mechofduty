#-*- coding: utf-8 -*-
'''
Created on 20-07-2013

@author: naster
'''

from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from mechofduty.gamer.models import Gamer

class GamerForm(ModelForm):
  class Meta:
    model = Gamer
    fields = ['name', 'profession']
        
class GamerCreationForm(UserCreationForm):
  email_duplicate = _("A user with that email already exist")
  class Meta:
    model = User
    fields = ('username', 'email')
        
  def clean_email(self):
    email = self.cleaned_data['email']
    try:
      User._default_manager.get(email=email)
    except User.DoesNotExist:
      return email
    raise ValidationError(self.email_duplicate, code='email_duplicate')  