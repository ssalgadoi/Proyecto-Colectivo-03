# Generated by Django 5.0.4 on 2024-04-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0006_rename_categories_post_category_and_more'),
        ('image', '0005_delete_category_alter_post_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='image_posts', to='history.category', verbose_name='Categoría'),
        ),
    ]
