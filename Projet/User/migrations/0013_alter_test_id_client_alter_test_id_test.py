# Generated by Django 4.0.3 on 2022-05-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_reponse_id_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='id_client',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='id_test',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
