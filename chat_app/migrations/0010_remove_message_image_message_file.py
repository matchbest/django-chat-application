# Generated by Django 4.2.4 on 2023-08-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0009_remove_message_file_message_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='image-message'),
        ),
    ]