# Generated by Django 3.2.3 on 2021-06-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_player_info_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_info',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
