# Generated by Django 2.1.4 on 2018-12-09 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181209_0554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table1',
            old_name='union',
            new_name='s_union',
        ),
    ]
