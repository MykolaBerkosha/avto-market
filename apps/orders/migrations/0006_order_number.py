# Generated by Django 3.0.13 on 2022-05-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20220404_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.IntegerField(blank=True, default=0, verbose_name='Number of parts'),
        ),
    ]