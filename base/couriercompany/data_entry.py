import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")
django.setup()

import xlrd
import MySQLdb
import math
from couriercompany.models import *


book = xlrd.open_workbook("base/Prepaid Pincode list.xlsx")
sheet = book.sheet_by_name("Prepaid")
first_sheet = book.sheet_by_index(0)
# for i in range(1, sheet.nrows):
# 	pvalue = str(first_sheet.cell(i, 0).value).split('.0')[0]
# 	obj = Citypincode.objects.get_or_create(pincode=pvalue)
# 	print pvalue
# 	obj[0].save()

courier_cells = [('Delhivery', 1, 2), ('Fedex', 3, 4), ('Dotzot', 5, 6), ('DTDC', 7, 'Notlimit'), ('Indiapost', 8, 'Notlimit')]

for i in range(1, sheet.nrows):
	pincode = str(first_sheet.cell(i,0).value).split('.0')[0]
	pincode_obj = Citypincode.objects.get(pincode=pincode)
	for courier_cell in courier_cells:
		courier_Details = Couriercompany.objects.get_or_create(pincode_id=pincode_obj, courier=courier_cell[0])[0]
		if first_sheet.cell(i, courier_cell[1]).value=='Y':
			courier_Details.availability = True
			courier_Details.limit = first_sheet.cell(i, courier_cell[2]).value if courier_cell[2] in [2, 4, 6] else courier_cell[2]
		for preference in range(9, 14):
			if first_sheet.cell(i, preference).value == courier_cell[0]:
				print "######################" 
				print first_sheet.cell(i, preference).value
				print courier_cell[0]
				print preference
				print "######################" 
				courier_Details.preference = preference - 8
		courier_Details.save()
	print pincode
	
	
	
