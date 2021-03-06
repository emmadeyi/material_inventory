# Generated by Django 3.0.5 on 2020-04-27 22:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='requisition/%Y/%m/%d/')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('staff_id', models.CharField(blank=True, max_length=10)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
