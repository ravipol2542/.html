# Generated by Django 3.0 on 2020-09-06 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0004_auto_20200906_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='stud',
        ),
    ]