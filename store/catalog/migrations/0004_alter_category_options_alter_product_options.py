# Generated by Django 5.0.4 on 2024-05-23 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_is_published_alter_image_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
