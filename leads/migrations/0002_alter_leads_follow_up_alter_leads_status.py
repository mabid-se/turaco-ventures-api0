# Generated by Django 5.1.2 on 2024-10-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='follow_up',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='leads',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]
