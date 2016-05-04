from rest_framework import serializers
from couriercompany.models import Couriercompany




class CouriercompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Couriercompany
		fields = ('courier', 'availability', 'limit', 'preference')


class CitypincodeSerializer(serializers.ModelSerializer):
	couriercompanies = CouriercompanySerializer(many=True, read_only=True)
	class Meta:
		model = Citypincode
		fields = ('pincode', 'couriercompanies')