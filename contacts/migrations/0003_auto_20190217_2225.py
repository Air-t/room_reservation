# Generated by Django 2.1.5 on 2019-02-17 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190217_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to='avatar'),
        ),
    ]
