# Generated by Django 4.0.3 on 2022-04-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_alter_taskmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
