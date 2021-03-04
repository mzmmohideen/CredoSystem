# Generated by Django 3.1.6 on 2021-03-04 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0002_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('reg_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('course_name', models.CharField(choices=[('B.E', 'B.E'), ('M.B.A', 'M.B.A'), ('M.E', 'M.E'), ('M.C.A', 'M.C.A'), ('Other', 'Other')], default='Other', max_length=10)),
                ('digital_brochure', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=5)),
            ],
        ),
    ]