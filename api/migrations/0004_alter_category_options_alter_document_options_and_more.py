# Generated by Django 5.1.7 on 2025-03-10 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_contactmessage_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'الفئات', 'verbose_name_plural': 'الفئات'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'المستندات', 'verbose_name_plural': 'المستندات'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'المنتجات', 'verbose_name_plural': 'المنتجات'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'الصور في الصفحة الرئيسية', 'verbose_name_plural': 'الصور في الصفحة الرئيسية'},
        ),
        migrations.AlterModelOptions(
            name='solution',
            options={'verbose_name': 'الحلول', 'verbose_name_plural': 'الحلول'},
        ),
    ]
