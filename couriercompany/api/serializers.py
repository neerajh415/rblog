from rest_framework import serializers
from couriercompany.models import Couriercompany

class CouriercompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Couriercompany
		fields = [
				'courier', 
				'availability', 
				'limit', 
				'preference',
				'pincode',
				]


class PostCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Couriercompany
		fields = [
				'courier', 
				'availability', 
				'limit', 
				'preference',
				'pincode',
				]	

class PreferencesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Couriercompany
		fields = [
				# 'courier', 
				# 'availability', 
				'limit', 
				# 'preference',
				'pincode',
				]
