# Generated by Django 3.0.13 on 2022-04-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20220404_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_post',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_self',
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('NOVA-POSHTA', 'Nova-poshta'), ('UKR-POSHTA', 'Ukr-poshta'), ('Delivery-POSHTA', 'Delivery-poshta'), ('SELF-PICKUP', 'Self-pickup')], default='SELF-PICKUP', max_length=22),
        ),
    ]
