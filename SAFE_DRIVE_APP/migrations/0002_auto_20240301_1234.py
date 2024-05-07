# Generated by Django 3.2.24 on 2024-03-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAFE_DRIVE_APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance_table',
            name='Type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ambulance_table',
            name='make_model',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ambulance_table',
            name='ownership',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ambulance_table',
            name='vehicle_no',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
