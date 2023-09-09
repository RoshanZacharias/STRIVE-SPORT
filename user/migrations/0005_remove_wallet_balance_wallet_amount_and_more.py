# Generated by Django 4.2.3 on 2023-08-24 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='balance',
        ),
        migrations.AddField(
            model_name='wallet',
            name='amount',
            field=models.FloatField(default=100),
        ),
        migrations.AddField(
            model_name='wallet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
