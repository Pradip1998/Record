# Generated by Django 3.1 on 2020-10-22 03:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recordekeep', '0003_auto_20201021_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('messege', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='customers',
            name='insertdate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
