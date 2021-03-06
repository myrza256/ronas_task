# Generated by Django 3.2.8 on 2021-10-28 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('main', models.CharField(max_length=255, verbose_name='main')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('temp_c', models.FloatField(default=0, verbose_name='temp_c')),
                ('temp_f', models.FloatField(default=0, verbose_name='temp_f')),
                ('humidity', models.PositiveIntegerField(default=0, verbose_name='humidity')),
                ('wind_speed', models.PositiveIntegerField(default=0, verbose_name='wind speed')),
                ('wind_deg', models.IntegerField(default=0, verbose_name='wind degree')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
            ],
            options={
                'verbose_name': 'weather',
                'verbose_name_plural': 'weather',
            },
        ),
    ]
