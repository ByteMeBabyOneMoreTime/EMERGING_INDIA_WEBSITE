# Generated by Django 5.0.6 on 2024-08-23 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_footer_and_home_page_data_become_a_partner_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer_and_home_page_data',
            name='about_us_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
