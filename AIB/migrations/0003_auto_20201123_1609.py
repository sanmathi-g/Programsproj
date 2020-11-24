# Generated by Django 3.1.3 on 2020-11-23 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AIB', '0002_auto_20201120_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_title', models.CharField(max_length=50)),
                ('Category_summary', models.CharField(max_length=200)),
                ('Category_slug', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='programs',
            name='prog_slug',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.CreateModel(
            name='ProgSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_series', models.CharField(max_length=50)),
                ('series_summary', models.CharField(max_length=200)),
                ('Category_title', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='AIB.progcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Series',
            },
        ),
        migrations.AddField(
            model_name='programs',
            name='prog_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='AIB.progseries', verbose_name='Series'),
        ),
    ]