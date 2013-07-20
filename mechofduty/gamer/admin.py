#-*- coding: utf-8 -*-
from django.contrib import admin
from mechofduty.gamer.models import Gamer, Statistic

class GamerAdmin(admin.ModelAdmin):
	pass

class StatisticAdmin(admin.ModelAdmin):
	pass

admin.site.register(Gamer, GamerAdmin)
admin.site.register(Statistic, StatisticAdmin)