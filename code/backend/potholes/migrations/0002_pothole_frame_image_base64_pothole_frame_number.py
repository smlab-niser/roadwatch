# Generated by Django 5.2.4 on 2025-07-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potholes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pothole',
            name='frame_image_base64',
            field=models.TextField(blank=True, help_text='Base64 encoded image data from CSV frame', null=True),
        ),
        migrations.AddField(
            model_name='pothole',
            name='frame_number',
            field=models.PositiveIntegerField(blank=True, help_text='Frame number from the original data collection', null=True),
        ),
    ]
