# Generated by Django 3.0.4 on 2020-05-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ili',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
