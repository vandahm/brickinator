# Generated by Django 5.1.6 on 2025-02-14 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='plate_width',
            field=models.CharField(choices=[('8x8', '8x8'), ('16x16', '16x16')], default='8x8', max_length=20),
        ),
    ]
