# Generated by Django 3.1.7 on 2021-04-21 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20210419_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
