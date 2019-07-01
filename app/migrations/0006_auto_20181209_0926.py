# Generated by Django 2.1.4 on 2018-12-09 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_table1'),
    ]

    operations = [
        migrations.CreateModel(
            name='school_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=200)),
                ('school_id', models.CharField(max_length=200)),
                ('zilla', models.CharField(max_length=200)),
                ('upazilla', models.CharField(max_length=200)),
                ('mouza', models.CharField(max_length=200)),
                ('union', models.CharField(max_length=200)),
                ('village', models.CharField(max_length=200)),
                ('no_of_village', models.IntegerField()),
                ('construction_year', models.CharField(max_length=200)),
                ('acc_cap_per', models.CharField(max_length=200)),
                ('acc_cap_ls', models.CharField(max_length=200)),
                ('plinth_area', models.FloatField()),
                ('land_area', models.FloatField()),
                ('northing', models.FloatField()),
                ('easting', models.FloatField()),
                ('population', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('expected_population', models.IntegerField()),
                ('existing', models.IntegerField()),
                ('under_construction', models.IntegerField()),
                ('ground_floor_uses', models.CharField(max_length=200)),
                ('g_others_uses', models.CharField(max_length=200)),
                ('first_floor_uses', models.CharField(max_length=200)),
                ('f_others_uses', models.CharField(max_length=200)),
                ('second_floor_uses', models.CharField(max_length=200)),
                ('s_others_uses', models.CharField(max_length=200)),
                ('third_floor_uses', models.CharField(max_length=200)),
                ('t_others_uses', models.CharField(max_length=200)),
                ('update_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='table',
        ),
    ]
