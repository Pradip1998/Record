# Generated by Django 3.1 on 2020-10-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.DateTimeField(auto_now_add=True, null=True)),
                ('country', models.CharField(max_length=100)),
                ('permanentadd', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('passwordnum', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('maritalstatus', models.BooleanField(default=False)),
            ],
        ),
    ]