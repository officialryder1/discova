# Generated by Django 5.0.4 on 2024-04-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_companyprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='co_owner_image',
            field=models.ImageField(blank=True, null=True, upload_to='company_logo'),
        ),
    ]