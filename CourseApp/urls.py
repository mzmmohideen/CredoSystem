# from django.urls import path
# from .views import CourseView
from rest_framework import routers
from .viewsets import *


CourseRouter = routers.DefaultRouter()

CourseRouter.register(r'course', CourseViewSet)
CourseRouter.register(r'product', ProductViewSet)
CourseRouter.register(r'customer', CustomerViewSet)
CourseRouter.register(r'registration', RegistrationViewSet)
