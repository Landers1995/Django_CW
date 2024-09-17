# Generated by Django 4.2.16 on 2024-09-17 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_rename_users_mailing_user_rename_users_message_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('email',), 'permissions': [('can_view_clients', 'can view clients'), ('can_edit_is_active', 'can edit active clients'), ('can_delete_clients', 'can delete clients')], 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ('interval',), 'permissions': [('can_view_mailing', 'can view mailing'), ('can_edit_is_active', 'can edit active mailing'), ('can_change_mailing', 'can change mailing'), ('can_delete_mailing', 'can delete mailing'), ('can_create_mailing', 'can create mailing')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
