# Generated by Django 4.2.3 on 2023-08-25 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0014_rename_discount_percentage_offer_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='discount',
            new_name='discount_percentage',
        ),
    ]
