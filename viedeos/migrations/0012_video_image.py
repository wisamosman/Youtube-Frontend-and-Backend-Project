# Generated by Django 4.2.3 on 2023-08-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viedeos', '0011_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(default='', upload_to='viedeos'),
            preserve_default=False,
        ),
    ]
