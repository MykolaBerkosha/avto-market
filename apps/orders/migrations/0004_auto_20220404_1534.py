# Generated by Django 3.0.13 on 2022-04-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20220404_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_post',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_self',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
