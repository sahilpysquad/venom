# Generated by Django 4.0.1 on 2023-02-27 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vc', '0002_vc_name_alter_vc_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vc',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='vc',
            name='emi_amount',
            field=models.PositiveBigIntegerField(default=1000, verbose_name='EMI Amount'),
        ),
    ]
