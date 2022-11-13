# Generated by Django 3.2 on 2022-11-12 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20221112_2127'),
        ('person', '0008_alter_person_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='healthprofessional',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='healthprofessional',
            name='work_modality',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='healthinsurance',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('ticket', models.FileField(upload_to='')),
                ('payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modality', models.CharField(default='', max_length=50)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.patient')),
                ('professional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.healthprofessional')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('LUNES', 'Lunes'), ('MARTES', 'Martes'), ('MIERCOLES', 'Miércoles'), ('JUEVES', 'Jueves'), ('VIERNES', 'Viernes'), ('SABADO', 'Sabado'), ('DOMINGO', 'Domingo')], default='', max_length=10)),
                ('start_time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('courses', models.ManyToManyField(to='person.Course')),
            ],
        ),
        migrations.CreateModel(
            name='PersonInEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ORGANIZADOR', 'Organizador'), ('PARTICIPANTE', 'Participante'), ('DONANTE', 'Donante')], default='', max_length=50)),
                ('events', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
                ('persons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.person')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.person'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=500)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.person')),
            ],
        ),
    ]
