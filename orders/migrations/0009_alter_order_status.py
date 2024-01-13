# Generated by Django 4.2.7 on 2024-01-09 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_order_product_order_carts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Новий', 'Новий'), ('Прийнято', 'Прийнято'), ('Скасовано', 'Скасовано'), ('Оплачено', 'Оплачено'), ('В дорозі', 'В дорозі')], default='Новий', max_length=20, verbose_name='Статус'),
        ),
    ]
