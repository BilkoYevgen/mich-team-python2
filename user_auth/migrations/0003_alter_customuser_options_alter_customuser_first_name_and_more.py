# Generated by Django 4.2.7 on 2023-12-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_customuser_is_subscribed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'користувача', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активний'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Адмін'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_subscribed',
            field=models.BooleanField(default=False, verbose_name='Підписан'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Призвище'),
        ),
    ]