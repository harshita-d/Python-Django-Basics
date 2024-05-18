# Generated by Django 5.0.4 on 2024-05-18 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('storyline', models.CharField(max_length=500)),
                ('active', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='platformlist',
            name='website',
            field=models.URLField(),
        ),
        migrations.DeleteModel(
            name='WatchList',
        ),
    ]
