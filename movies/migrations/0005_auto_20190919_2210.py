# Generated by Django 2.2.5 on 2019-09-19 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20190919_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imdbinfo',
            name='imdbid',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='imdbinfo',
            name='imdbrating',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='imdbinfo',
            name='imdbvotes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='imdbinfo',
            name='metascore',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='marketinginfo',
            name='awards',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='marketinginfo',
            name='boxoffice',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='marketinginfo',
            name='poster',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='marketinginfo',
            name='production',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='marketinginfo',
            name='rated',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='marketinginfo',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='rating',
            name='source',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='staff',
            name='actors',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='staff',
            name='director',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='staff',
            name='writer',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='dvd',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='relased',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='year',
            field=models.DateField(blank=True),
        ),
    ]
