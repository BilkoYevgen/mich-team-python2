# Generated by Django 4.2.7 on 2024-01-06 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_size_alter_cart_session_id'),
        ('orders', '0006_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='cart.cart', verbose_name='Товар'),
        ),
    ]
