# Generated by Django 3.1.6 on 2021-02-24 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='remark',
        ),
    ]
