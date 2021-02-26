from django.contrib import admin
from .models import Course, Product, Customer
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass