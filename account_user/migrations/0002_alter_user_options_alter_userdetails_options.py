# Generated by Django 4.0.1 on 2023-02-24 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='userdetails',
            options={'verbose_name': 'User Detail', 'verbose_name_plural': 'User Details'},
        ),
    ]
