# Generated by Django 4.1.6 on 2023-02-07 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Term_Taxonomy',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='commentmeta',
            old_name='comment_id',
            new_name='comment',
        ),
        migrations.DeleteModel(
            name='Term_Relationship',
        ),
    ]
