# Generated by Django 4.1.4 on 2023-02-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_ping_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('published', 'published'), ('Scheduled', 'Scheduled')], default='published', max_length=20),
        ),
    ]
