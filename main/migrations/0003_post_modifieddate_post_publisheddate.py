# Generated by Django 4.1.3 on 2023-01-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='modifiedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='publishedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]