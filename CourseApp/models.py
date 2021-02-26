from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100, default='BE', null=True)
    course_duration  = models.IntegerField()

    def __str__(self):
        return self.course_name

    # class meta:
    #     db_table = 'course'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(default=None)
    qty = models.IntegerField()

    def __str__(self):
        return "%s-%s"%(self.product_name, self.product_id)

class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s-%s"%(self.cus_name, self.cus_id)
