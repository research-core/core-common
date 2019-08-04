# Generated by Django 2.2.4 on 2019-08-03 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('short_name', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
