# Generated by Django 3.0.13 on 2022-04-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20220404_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.BooleanField(choices=[(True, 'Post ofice'), (False, 'Self-pickup')], default=True, max_length=22),
        ),
    ]