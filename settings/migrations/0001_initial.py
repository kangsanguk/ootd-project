# Generated by Django 3.0.3 on 2020-07-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('left_credit', models.CharField(max_length=120)),
                ('right_credit', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('footer_1', models.TextField()),
                ('email', models.EmailField(max_length=50)),
                ('facebook', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('youtube', models.CharField(max_length=50)),
            ],
        ),
    ]
