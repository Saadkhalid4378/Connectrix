# Generated by Django 5.0.1 on 2024-01-18 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thought', '0002_comment_reply_text_alter_comment_thought'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='thought.comment'),
        ),
    ]
