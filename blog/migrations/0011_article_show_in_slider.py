# Generated by Django 3.1.3 on 2020-12-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201213_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='show_in_slider',
            field=models.BooleanField(default=False, verbose_name='نمایش در اسلایدر'),
        ),
    ]
