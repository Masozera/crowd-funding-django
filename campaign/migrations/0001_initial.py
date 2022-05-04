# Generated by Django 3.1.7 on 2021-04-01 00:30

import campaign.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('details', models.TextField(max_length=2000)),
                ('target', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=campaign.models.in_fourteen_days)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='CommentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=2000, verbose_name='Report details')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000, verbose_name='Comment')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=2000)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to='static/images/', verbose_name='Image')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campaign.category'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
