# Generated by Django 3.1.7 on 2021-03-28 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210327_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
