# Generated by Django 4.2.5 on 2023-09-27 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_experience', '0003_alter_workexperience_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workexperience',
            options={'ordering': ['-start_date', '-end_date']},
        ),
    ]
