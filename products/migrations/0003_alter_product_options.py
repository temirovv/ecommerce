# Generated by Django 5.0.6 on 2024-12-25 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Mahsulot', 'verbose_name_plural': 'Mahsulotlar'},
        ),
    ]
