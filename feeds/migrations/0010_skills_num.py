# Generated by Django 3.2.6 on 2021-11-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0009_auto_20211128_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
