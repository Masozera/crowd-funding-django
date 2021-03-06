# Generated by Django 3.1.7 on 2021-03-31 23:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.IntegerField(validators=[django.core.validators.RegexValidator('^01[0-2][0-9]{8}$', 'Egyptian phone number is required')])),
                ('avatar', models.ImageField(upload_to='images/')),
                ('is_admin', models.BooleanField(default=False)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('fb_account', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
