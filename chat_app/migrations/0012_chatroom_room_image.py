# Generated by Django 4.2.4 on 2023-08-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0011_remove_message_file_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='room_image',
            field=models.ImageField(blank=True, null=True, upload_to='room-image'),
        ),
    ]
