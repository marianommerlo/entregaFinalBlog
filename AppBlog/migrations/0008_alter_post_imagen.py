# Generated by Django 4.0.5 on 2022-06-12 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0007_alter_post_cuerpo_alter_post_subtitulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.URLField(max_length=1100),
        ),
    ]
