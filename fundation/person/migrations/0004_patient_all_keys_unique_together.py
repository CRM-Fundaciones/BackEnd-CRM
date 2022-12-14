# Generated by Django 3.2 on 2022-09-18 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_alter_patient_person'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='patient',
            constraint=models.UniqueConstraint(fields=('person', 'care_taker'), name='all_keys_unique_together'),
        ),
    ]
