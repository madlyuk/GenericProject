# Generated by Django 2.2.7 on 2020-01-24 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appModuli', '0004_auto_20191224_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appmoduli',
            name='appUrl',
        ),
        migrations.AddField(
            model_name='appmoduli',
            name='mainAppView',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='main View'),
            preserve_default=False,
        ),
    ]
