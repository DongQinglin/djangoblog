# Generated by Django 3.0 on 2019-12-06 12:14

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(null=True, upload_to='media/article_img/%Y/%m/%d/', verbose_name='文章图片'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='media/banner/', verbose_name='轮播图'),
        ),
    ]
