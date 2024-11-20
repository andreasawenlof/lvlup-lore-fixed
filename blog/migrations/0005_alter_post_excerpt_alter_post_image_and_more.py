# Generated by Django 4.2.16 on 2024-11-19 12:50

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='images/logo/logo6.webp', force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_alt',
            field=models.CharField(default='Describe the image', max_length=100),
        ),
    ]