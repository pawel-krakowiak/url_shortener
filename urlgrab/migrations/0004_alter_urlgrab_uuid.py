# Generated by Django 4.0.6 on 2022-07-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlgrab', '0003_remove_urlgrab_shorted_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlgrab',
            name='uuid',
            field=models.CharField(max_length=10),
        ),
    ]
