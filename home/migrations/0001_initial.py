# Generated by Django 3.1.2 on 2020-10-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('account_sid', models.CharField(max_length=100)),
                ('auth_token', models.CharField(max_length=100)),
                ('twillo_number', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_from', models.CharField(max_length=50)),
                ('msg_to', models.CharField(max_length=50)),
                ('msg', models.CharField(max_length=50)),
                ('account_type', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('created_at', models.TimeField()),
                ('updated_at', models.TimeField()),
            ],
            options={
                'db_table': 'msg_single',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]