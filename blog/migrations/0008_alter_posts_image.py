# Generated by Django 4.0.4 on 2022-06-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_alter_posts_image_alter_posts_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y'),
        ),
    ]
