# Generated by Django 5.0 on 2024-04-12 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_article_last_modified_article_categories_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'catagories'},
        ),
    ]
