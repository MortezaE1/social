# Generated by Django 4.0.6 on 2022-08-25 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
