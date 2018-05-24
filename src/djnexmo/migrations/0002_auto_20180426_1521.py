# Generated by Django 2.0.4 on 2018-04-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("djnexmo", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="smsmessagepart",
            name="data",
            field=models.BinaryField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name="smsmessagepart",
            name="keyword",
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name="smsmessagepart",
            name="text",
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name="smsmessagepart",
            name="udh",
            field=models.BinaryField(max_length=160, null=True),
        ),
    ]
