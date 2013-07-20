#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Gamer(models.Model):
	PROFESSION = (('S', 'Żołnierz'),
				  ('M', 'Mechanik'),
				  ('E', 'Inżynier'),
				  ('G', 'Geolog'),
				  )
	user = models.OneToOneField(User)
	name = models.CharField('Nazwa gracza', max_length=30)
	profession = models.CharField('Profesja gracza', max_length=4, choices=PROFESSION)
	
	def __unicode__(self):
		return self.name
	
class Statistic(models.Model):
	gamer = models.OneToOneField(Gamer)
	experience = models.BigIntegerField('Doświadczenie', default=0)
	
	strength = models.IntegerField('Siła', default=5)
	dexterity = models.IntegerField('Zręczność', default=5)
	stamina = models.IntegerField('Wytrzymałość', default=5)
	intelligence = models.IntegerField('Inteligencja', default=5)
	mechanice = models.IntegerField('Mechanika', default=5)
	knowladge = models.IntegerField('Wiedza', default=5)
	dodge = models.IntegerField('Unik', default=5)	
	skill_point = models.IntegerField('Punkty umiejętności', default=0)
	
	def __unicode__(self):
		return "Statistic: %s" % self.gamer.name 
	
	def get_level(self):
		# @TODO konieczna implementacja wzoru
		return 1