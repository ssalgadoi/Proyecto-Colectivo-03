# Generated by Django 5.0.4 on 2024-04-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_remove_post_categories_remove_post_url_post_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='data',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Url del proyecto'),
        ),
    ]
