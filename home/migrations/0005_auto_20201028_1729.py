# Generated by Django 3.1.2 on 2020-10-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201028_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message2',
            name='msg_to',
            field=models.CharField(max_length=100),
        ),
    ]
