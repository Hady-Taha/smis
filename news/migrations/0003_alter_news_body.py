# Generated by Django 4.0.2 on 2022-02-21 13:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_news_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
