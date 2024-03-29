# Generated by Django 2.2.6 on 2019-10-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20191025_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('contact', models.EmailField(max_length=254)),
            ],
        ),
    ]
