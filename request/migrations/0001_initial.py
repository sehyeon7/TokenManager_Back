# Generated by Django 4.2.6 on 2023-11-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
                ('spec_url', models.CharField(max_length=64)),
            ],
        ),
    ]
