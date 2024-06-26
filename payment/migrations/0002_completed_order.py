# Generated by Django 4.1 on 2024-04-03 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0002_rename_user_merchant_author'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant.merchant')),
            ],
        ),
    ]
