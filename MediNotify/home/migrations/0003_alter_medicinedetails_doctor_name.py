# Generated by Django 3.2.10 on 2022-07-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220713_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedetails',
            name='doctor_name',
            field=models.CharField(max_length=128),
        ),
    ]
