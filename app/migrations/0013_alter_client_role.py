# Generated by Django 4.0.2 on 2022-02-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_expensedehqon_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='role',
            field=models.CharField(blank=True, choices=[('dehqon', 'Dehqon'), ('client', 'Qushxona Klienti(Sotib oluvhi)'), ('sotuvchi', 'Bozordagi sotuvchi'), ('kallahasb', 'Kalla hasb oluvchi sotuvchi'), ('Teri', 'Teri oluvchi sotuvchi')], max_length=125, null=True),
        ),
    ]
