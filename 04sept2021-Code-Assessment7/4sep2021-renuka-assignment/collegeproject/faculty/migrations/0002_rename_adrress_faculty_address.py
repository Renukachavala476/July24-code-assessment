# Generated by Django 3.2.6 on 2021-09-04 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='adrress',
            new_name='address',
        ),
    ]
