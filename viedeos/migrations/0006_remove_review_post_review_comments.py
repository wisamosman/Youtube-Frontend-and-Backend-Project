# Generated by Django 4.2.3 on 2023-07-30 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viedeos', '0005_video_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='post',
        ),
        migrations.AddField(
            model_name='review',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments_review', to='viedeos.video'),
        ),
    ]
