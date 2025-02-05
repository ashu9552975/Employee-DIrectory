# Generated by Django 5.0.6 on 2024-06-19 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_rename_job_title_member_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.department'),
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.role'),
        ),
    ]
