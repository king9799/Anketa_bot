# Generated by Django 3.2.7 on 2021-10-09 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_clients_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='yaqin_qar',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
