from rest_framework import viewsets, authtoken
from .serializers import *


class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

	# def create(self, request, *args, **kwargs):
	# 	pass

	# def get(self):
	# 	for i in self.queryset:
	# 		reg = Registration.objects.filter(course_id = i.id)
	# 		i.add(reg)


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
	queryset = Registration.objects.all()
	serializer_class = RegistrationSerializer





# models -> serializers -> viewsets -> urls