# Generated by Django 5.1.3 on 2024-11-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='student_images/'),
        ),
    ]
