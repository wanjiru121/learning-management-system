# Generated by Django 2.2.6 on 2019-10-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='marital_status',
            field=models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('W', 'Widowed'), ('D', 'Divorced'), ('SE', 'Separated'), ('P', 'Partnered')], default=None, max_length=1),
        ),
    ]