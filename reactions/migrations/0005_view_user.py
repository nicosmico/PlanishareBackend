# Generated by Django 4.0.3 on 2022-06-09 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reactions', '0004_alter_view_firebaseuseruuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
