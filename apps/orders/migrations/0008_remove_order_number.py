# Generated by Django 3.0.13 on 2022-05-11 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20220511_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
    ]
