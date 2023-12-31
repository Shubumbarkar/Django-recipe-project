# Generated by Django 4.2.7 on 2023-12-01 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='first_name',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='last_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='role',
            name='last_name',
        ),
    ]
