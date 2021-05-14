# Generated by Django 3.2 on 2021-05-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_bed_oxygen_plasma'),
    ]

    operations = [
        migrations.CreateModel(
            name='nHelp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=12)),
                ('plasma', models.BooleanField(default=False)),
                ('bed', models.BooleanField(default=False)),
                ('oxygen', models.BooleanField(default=False)),
                ('date', models.DateField()),
            ],
        ),
    ]