# Generated by Django 4.2.16 on 2024-09-16 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0002_mailing_users_message_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор рассылки'),
        ),
        migrations.AlterField(
            model_name='message',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор сообщения'),
        ),
    ]
