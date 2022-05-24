# Generated by Django 4.0.4 on 2022-05-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('C', 'construction'), ('W', 'welding'), ('G', 'general'), ('P', 'paints')], default='C', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('C', 'construction'), ('W', 'welding'), ('G', 'general'), ('P', 'paints')], default='P', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]