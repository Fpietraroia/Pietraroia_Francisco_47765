# Generated by Django 4.2.5 on 2023-10-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0007_alter_userprofile_chosen_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='chosen_avatar',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
