# Generated by Django 2.2.3 on 2019-10-29 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_manager', '0002_auto_20191029_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillrubricks',
            old_name='name',
            new_name='skill',
        ),
    ]
