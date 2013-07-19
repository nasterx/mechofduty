from django.db import models
from django.contrib.auth.models import User

class Gamer(models.Model):
	name = models.TextField('Nazwa gracza')
	user = models.OneToOneField(User)
