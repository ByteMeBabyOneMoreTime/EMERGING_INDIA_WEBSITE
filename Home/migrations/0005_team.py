# Generated by Django 5.0.6 on 2024-07-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_rename_navigation_links_navigation_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='team/')),
                ('Name', models.CharField(max_length=250)),
                ('Position', models.CharField(max_length=200)),
                ('Organiztion', models.CharField(max_length=400)),
            ],
        ),
    ]
