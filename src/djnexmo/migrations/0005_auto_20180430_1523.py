# Generated by Django 2.0.4 on 2018-04-30 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djnexmo', '0004_auto_20180427_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smsmessagepart',
            options={'ordering': ('-concat_ref', 'concat_part'), 'verbose_name': 'Message Part', 'verbose_name_plural': 'Message Parts'},
        ),
    ]
