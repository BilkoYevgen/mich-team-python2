# Generated by Django 4.2.7 on 2024-01-09 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_order_carts'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=2424, max_length=40, verbose_name='Пошта'),
            preserve_default=False,
        ),
    ]
