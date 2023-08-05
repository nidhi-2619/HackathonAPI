# Generated by Django 4.2.3 on 2023-08-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0005_alter_submission_hackathon_alter_submission_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='file',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='image',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='link',
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_type',
            field=models.FileField(choices=[('image', 'Image'), ('file', 'File'), ('link', 'Link')], max_length=10, upload_to=''),
        ),
    ]
