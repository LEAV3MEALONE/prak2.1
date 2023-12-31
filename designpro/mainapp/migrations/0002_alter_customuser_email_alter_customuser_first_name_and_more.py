# Generated by Django 4.2.7 on 2023-11-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='patronymic',
            field=models.CharField(max_length=200, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=200, unique=True, verbose_name='Логин'),
        ),
    ]
