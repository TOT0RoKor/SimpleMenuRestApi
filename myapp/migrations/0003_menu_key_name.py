# Generated by Django 2.0.5 on 2018-05-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='key_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]