# Generated by Django 4.1.3 on 2023-01-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Lng',
            field=models.FloatField(null=True),
        ),
    ]