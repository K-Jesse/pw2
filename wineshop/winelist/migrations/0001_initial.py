# Generated by Django 4.0.4 on 2022-05-24 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('year', models.IntegerField()),
                ('flavour', models.CharField(max_length=3000)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
