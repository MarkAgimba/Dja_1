# Generated by Django 2.2.1 on 2019-05-13 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        # migrations.CreateModel(
        #     name='Location',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(max_length=30)),
        #     ],
        # ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image_url', models.ImageField(blank=True, upload_to='images/')),
                ('categories', models.ManyToManyField(to='mpic.categories')),
                # ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='mpic.Location')),
            ],
        ),
    ]
