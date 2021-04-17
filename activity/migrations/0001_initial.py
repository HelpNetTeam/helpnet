# Generated by Django 3.2 on 2021-04-17 00:50

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NeedActivity',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='NeedUom',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('responsible_id', models.IntegerField(null=True)),
                ('website', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.CharField(choices=[('1', 'Bad'), ('2', 'Kinda Bad'), ('3', 'Normal'), ('4', 'Great'), ('5', 'Excellent')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('address', models.TextField(null=True)),
                ('country_id', models.IntegerField(null=True)),
                ('state_id', models.IntegerField(null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'activities',
            },
        ),
    ]
