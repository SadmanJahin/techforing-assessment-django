# Generated by Django 3.2.7 on 2021-12-29 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academy', '0005_coursepurchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='product_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
