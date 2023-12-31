# Generated by Django 4.2.5 on 2023-10-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='education_images')),
                ('achievement', models.CharField(max_length=150)),
                ('institution', models.CharField(blank=True, max_length=200, null=True)),
                ('date_achieved', models.DateField()),
                ('valid_until', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date_achieved'],
            },
        ),
    ]
