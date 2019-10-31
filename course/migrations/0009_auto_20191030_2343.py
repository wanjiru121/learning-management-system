# Generated by Django 2.2.6 on 2019-10-30 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_coursecalendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lessons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.LessonPlan'),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Assignment'),
        ),
    ]
