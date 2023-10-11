# Generated by Django 4.2.5 on 2023-10-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0004_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pacientes',
            name='id',
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='documento',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='chosen_avatar',
            field=models.CharField(choices=[('avatar1.jpg', 'Avatar 1'), ('avatar2.png', 'Avatar 2')], max_length=255),
        ),
    ]