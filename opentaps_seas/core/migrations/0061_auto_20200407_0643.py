# Generated by Django 2.2.10 on 2020-04-07 13:43

import cratedb.fields.array
import cratedb.fields.hstore
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_auto_20200325_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meter',
            name='rate_plan',
        ),
        migrations.AlterField(
            model_name='meterrateplanhistory',
            name='rate_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.MeterRatePlan'),
        ),
    ]
