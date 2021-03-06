# Generated by Django 3.0.4 on 2020-05-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20200526_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='aidat',
            field=models.IntegerField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='balkonsayisi',
            field=models.IntegerField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='banyosayisi',
            field=models.IntegerField(default=1, max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='esyali',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], default=False, max_length=10),
            preserve_default=False,
        ),
    ]
