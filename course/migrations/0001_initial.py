# Generated by Django 2.2.6 on 2019-10-13 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('course_id', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('start_date', models.DateField(help_text='format: YYYY-MM-DD', max_length=10, null=True)),
                ('end_date', models.DateField(help_text='format: YYYY-MM-DD', max_length=10, null=True)),
                ('course_email', models.EmailField(max_length=254)),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainer.Trainer')),
            ],
        ),
    ]