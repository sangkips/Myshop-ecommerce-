# Generated by Django 4.0.4 on 2022-05-24 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category_product_label_alter_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='label',
        ),
    ]
