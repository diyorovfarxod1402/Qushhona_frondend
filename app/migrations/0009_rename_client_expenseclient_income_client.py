# Generated by Django 4.0.2 on 2022-02-08 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_expenseclient_income_client_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenseclient',
            old_name='client',
            new_name='income_client',
        ),
    ]
