# Generated by Django 3.2.7 on 2022-01-07 06:35

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0014_events_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(choices_display='WITH_GMT_OFFSET', default='Europe/London'),
        ),
    ]
