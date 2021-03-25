from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Registration
		fields = '__all__'
