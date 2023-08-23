# Generated by Django 4.2.4 on 2023-08-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0006_message_file_alter_message_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, upload_to='image-message'),
        ),
    ]