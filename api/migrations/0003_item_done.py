# Generated by Django 4.2.1 on 2023-05-14 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
