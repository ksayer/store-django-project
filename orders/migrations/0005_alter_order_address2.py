# Generated by Django 3.2 on 2022-03-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
