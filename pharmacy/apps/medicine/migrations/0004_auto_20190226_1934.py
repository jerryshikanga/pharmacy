# Generated by Django 2.1.7 on 2019-02-26 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_medicine_advisable_units'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='units',
            new_name='intake_form',
        ),
    ]
