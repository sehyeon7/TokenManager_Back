# Generated by Django 4.2.6 on 2024-02-19 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0003_tokens_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokens',
            name='expires_at',
            field=models.CharField(max_length=256),
        ),
    ]