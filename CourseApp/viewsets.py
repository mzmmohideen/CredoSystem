from rest_framework import viewsets
from .serializers import *


class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


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