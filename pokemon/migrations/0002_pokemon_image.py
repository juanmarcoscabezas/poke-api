# Generated by Django 3.0.8 on 2021-01-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='image',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
