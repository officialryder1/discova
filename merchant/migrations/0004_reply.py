# Generated by Django 5.0.4 on 2024-04-09 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0003_messageadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='M2A_message')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant.messageadmin')),
            ],
        ),
    ]
