# Generated by Django 3.2 on 2022-11-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0009_auto_20221112_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('print_date', models.DateTimeField()),
                ('print_amount', models.IntegerField()),
                ('delivered_amount', models.IntegerField()),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ad_type', models.CharField(default='', max_length=50)),
                ('objective', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('comments', models.ManyToManyField(to='person.Comment')),
            ],
        ),
    ]
