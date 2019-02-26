# Generated by Django 2.1.7 on 2019-02-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('manufacture_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField()),
                ('units', models.CharField(choices=[('mg', 'mg'), ('ml', 'ml'), ('tablet', 'tablet')], max_length=20)),
            ],
        ),
    ]