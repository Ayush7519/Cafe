# Generated by Django 5.0.7 on 2024-09-09 02:18

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModelCms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, max_length=20, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CafeCms',
            fields=[
                ('basemodelcms_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.basemodelcms')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='cafe_cms_image')),
                ('cafe_email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='E-mail')),
                ('email_1', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='E-mail')),
                ('email_2', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='E-mail')),
                ('mobile_no1', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('((98)|(97))(\\d){8}', message="Please enter a valid Nepali phone number starting with '98' or '97' and consisting of 10 digits.")])),
                ('mobile_no2', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('((98)|(97))(\\d){8}', message="Please enter a valid Nepali phone number starting with '98' or '97' and consisting of 10 digits.")])),
                ('mobile_no3', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('((98)|(97))(\\d){8}', message="Please enter a valid Nepali phone number starting with '98' or '97' and consisting of 10 digits.")])),
                ('telephone', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^0\\d{1,2}\\d{6,7}$', message='Enter a valid telephone number')])),
                ('location', models.CharField(max_length=255)),
                ('pan_number', models.PositiveBigIntegerField(blank=True, null=True)),
                ('discount_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('additional_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            bases=('cms.basemodelcms',),
        ),
    ]
