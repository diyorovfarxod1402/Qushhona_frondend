# Generated by Django 4.0.2 on 2022-02-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_client_status_bozor'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomesotuvchi',
            name='status',
            field=models.CharField(blank=True, choices=[('progress', 'Jarayonda'), ('completed', 'yakunlandi')], default='progress', max_length=88, null=True),
        ),
    ]
