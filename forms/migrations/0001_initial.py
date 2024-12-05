# Generated by Django 5.0.6 on 2024-08-01 21:52

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Your_problem_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('whatsapp', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('teshil', models.CharField(max_length=120)),
                ('block', models.CharField(max_length=120)),
                ('thana', models.CharField(max_length=120)),
                ('tehsil', models.CharField(max_length=120)),
                ('village_or_town', models.CharField(max_length=120)),
                ('address', models.TextField()),
                ('issue_is_related_to', models.TextField(max_length=300)),
                ('Your_problem_state', models.CharField(max_length=200)),
                ('Your_problem_district', models.CharField(max_length=200)),
                ('Your_problem_teshil', models.CharField(max_length=120)),
                ('Your_problem_block', models.CharField(max_length=120)),
                ('Your_problem_thana', models.CharField(max_length=120)),
                ('Your_problem_tehsil', models.CharField(max_length=120)),
                ('Your_problem_village_or_town', models.CharField(max_length=120)),
                ('Your_problem_address', models.TextField()),
                ('document', models.URLField(blank=True, default=None, null=True)),
                ('picture', models.URLField(blank=True, default=None, null=True)),
                ('status', models.CharField(choices=[('Uploaded', 'Uploaded'), ('Approved', 'Aproved')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
