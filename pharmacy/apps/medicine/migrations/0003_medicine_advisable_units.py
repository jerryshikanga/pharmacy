# Generated by Django 2.1.7 on 2019-02-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_auto_20190226_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='advisable_units',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
