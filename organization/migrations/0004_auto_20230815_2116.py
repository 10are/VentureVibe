# Generated by Django 3.2.9 on 2023-08-15 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_organization_dislike_count_organization_like_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='dislike_count',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='like_count',
        ),
        migrations.DeleteModel(
            name='OrganizationRating',
        ),
    ]
