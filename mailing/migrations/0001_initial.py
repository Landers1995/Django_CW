# Generated by Django 4.2.16 on 2024-09-19 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Почта клиента"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Введите имя", max_length=50, verbose_name="Имя"
                    ),
                ),
                (
                    "second_name",
                    models.CharField(
                        help_text="Введите фамилию",
                        max_length=50,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "third_name",
                    models.CharField(
                        blank=True,
                        help_text="Введите отчество",
                        max_length=50,
                        null=True,
                        verbose_name="Отчество",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="Введите комментарий",
                        null=True,
                        verbose_name="Комментарий",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
                "ordering": ("email",),
                "permissions": [
                    ("can_edit_is_active_client", "can edit active clients")
                ],
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "send_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата начала рассылки"
                    ),
                ),
                (
                    "create_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Дата создания рассылки"
                    ),
                ),
                (
                    "update_date",
                    models.DateField(
                        auto_now=True, verbose_name="Дата изменения рассылки"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("completed", "completed"),
                            ("created", "created"),
                            ("started", "started"),
                        ],
                        default="created",
                        verbose_name="Статус рассылки",
                    ),
                ),
                (
                    "interval",
                    models.CharField(
                        choices=[
                            ("once a minute", "once a minute"),
                            ("once a day", "once a days"),
                            ("once a week", "once a week"),
                            ("once a month", "once a months"),
                        ],
                        default="once a day",
                        verbose_name="Интервал рассылки",
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата окончания рассылки"
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "ordering": ("interval",),
                "permissions": [
                    ("can_edit_is_active_mailing", "can edit active mailing")
                ],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок сообщения",
                        max_length=50,
                        verbose_name="Заголовок сообщения",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        help_text="Введите содержание сообщения",
                        verbose_name="Содержание сообщения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="TryMailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_try",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Дата последней попытки рассылки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("success", "success"), ("fail", "fail")],
                        default="success",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "response",
                    models.TextField(blank=True, null=True, verbose_name="Ответ"),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mailings",
                        to="mailing.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылок",
                "ordering": ("status",),
            },
        ),
    ]
