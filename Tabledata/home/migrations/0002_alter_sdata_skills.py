# Generated by Django 5.1.3 on 2024-12-06 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdata',
            name='Skills',
            field=models.CharField(max_length=30),
        ),
    ]
