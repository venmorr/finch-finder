# Generated by Django 4.2.6 on 2023-11-02 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_alter_feeding_options_alter_feeding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
