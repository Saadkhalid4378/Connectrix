# Generated by Django 5.0.1 on 2024-01-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thought', '0004_thought_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='text',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='thought',
            name='title',
            field=models.CharField(max_length=32),
        ),
    ]
