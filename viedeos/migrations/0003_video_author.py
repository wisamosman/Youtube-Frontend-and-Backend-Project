# Generated by Django 4.2.3 on 2023-07-30 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viedeos', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='video_author', to='viedeos.author'),
            preserve_default=False,
        ),
    ]
