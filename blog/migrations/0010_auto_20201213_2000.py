# Generated by Django 3.1.4 on 2020-12-13 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20201213_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created',), 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقاله\u200cها'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default='accounts.User', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
    ]
