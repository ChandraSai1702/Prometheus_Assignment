# Generated by Django 4.2.16 on 2024-10-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0002_task_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='task_files/'),
        ),
    ]