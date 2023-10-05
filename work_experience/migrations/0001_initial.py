# Generated by Django 4.2.5 on 2023-09-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='work_images')),
                ('company', models.CharField(max_length=140)),
                ('team_name', models.CharField(max_length=300)),
                ('job_title', models.CharField(max_length=140)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]