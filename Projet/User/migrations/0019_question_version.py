# Generated by Django 4.0.3 on 2022-05-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0018_client_is_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='version',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
