# Generated by Django 3.2.7 on 2021-09-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=40)),
                ('address', models.CharField(blank=True, default='', max_length=40)),
                ('clas', models.CharField(blank=True, default='', max_length=40)),
                ('mno', models.CharField(blank=True, default='', max_length=40)),
                ('username', models.CharField(blank=True, default='', max_length=40)),
                ('password', models.CharField(blank=True, default='', max_length=40)),
            ],
        ),
    ]
