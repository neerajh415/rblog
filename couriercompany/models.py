from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

COURIER_COMPANY_NAME = (
	('Delhivery', 'Delhivery'),
	('Fedex', 'Fedex'),
	('Dotzot', 'Dotzot'),
	('DTDC', 'DTDC'),
	('Indiapost', 'Indiapost'),
	)

PREFERENCE = (
	(1, 'Preference 1'),
	(2, 'Preference 2'),
	(3, 'Preference 3'),
	(4, 'Preference 4'),
	(5, 'Preference 5'),
	)
# Create your models here.
class Citypincode(models.Model):
	pincode = models.CharField(_('Pincode'), max_length=200, primary_key=True)

	def __unicode__(self):
		return self.pincode



class Couriercompany(models.Model):
	pincode = models.ForeignKey(Citypincode, related_name='couriercompanies')
	courier = models.CharField(choices=COURIER_COMPANY_NAME, default='Delhivery', max_length=200)
	limit = models.CharField(blank=True, null=True, max_length=50)
	availability = models.BooleanField(default=False)
	preference = models.IntegerField(choices=PREFERENCE, default=1)

	def __unicode__(self):
		return "%s" % self.courier