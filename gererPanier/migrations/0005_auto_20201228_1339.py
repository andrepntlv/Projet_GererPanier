# Generated by Django 2.2.17 on 2020-12-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gererPanier', '0004_auto_20201218_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
