# Generated by Django 4.1.4 on 2023-02-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_guid_alter_post_menu_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
