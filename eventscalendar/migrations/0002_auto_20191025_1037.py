# Generated by Django 2.2.6 on 2019-10-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventscalendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
