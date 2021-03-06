# Generated by Django 3.0.13 on 2022-01-12 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20211130_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visible', models.CharField(choices=[('visible', 'Visible'), ('invisible', 'Invisible')], default=True, max_length=255)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('logo', models.ImageField(upload_to='product_logos', verbose_name='Logo')),
                ('tags', models.TextField(blank=True, db_index=True, max_length=1000, verbose_name='Tags')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='categories.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
