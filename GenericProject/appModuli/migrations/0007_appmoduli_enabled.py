# Generated by Django 2.2.7 on 2020-02-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appModuli', '0006_auto_20200124_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='appmoduli',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
