# Generated by Django 3.1 on 2021-10-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]