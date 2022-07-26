# Generated by Django 3.2.7 on 2022-02-03 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BusinessSecurity', '0047_alter_subscriptionfield_subscriptionservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptionteam_subscriptionorder', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptionteam_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
