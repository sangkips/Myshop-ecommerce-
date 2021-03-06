# Generated by Django 4.0.4 on 2022-05-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('C', 'construction'), ('W', 'welding'), ('G', 'general'), ('P', 'paints')], default='P', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='S', max_length=1),
            preserve_default=False,
        ),
    ]
