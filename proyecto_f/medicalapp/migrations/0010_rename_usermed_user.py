# Generated by Django 4.2.5 on 2023-10-10 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('medicalapp', '0009_usermed_delete_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserMed',
            new_name='User',
        ),
    ]