# Generated by Django 3.0.4 on 2020-05-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_product_depozito'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='odasayisi',
            field=models.CharField(default='3+1', max_length=100),
        ),
    ]
