# Generated by Django 5.1.7 on 2025-04-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fireincident', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FireIncident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('severity_level', models.CharField(choices=[('Minor', 'Minor'), ('Moderate', 'Moderate'), ('Major', 'Major')], max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fire_incident',
            },
        ),
        migrations.RemoveField(
            model_name='firestation',
            name='location',
        ),
        migrations.AddField(
            model_name='firestation',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=3, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firestation',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locations',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='firestation',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
