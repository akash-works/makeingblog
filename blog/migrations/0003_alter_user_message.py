# Generated by Django 4.1.6 on 2023-02-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
