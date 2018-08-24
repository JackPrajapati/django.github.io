from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
	user_rec = models.ForeignKey(User,default=True)
	address_one = models.CharField(max_length=100,default=True)
	address_two = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=50,blank=True)
	state = models.CharField(max_length=20,blank=True)

	def __unicode__(self):
		return u"%s" % self.user_rec