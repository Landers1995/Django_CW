from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):

    email = models.EmailField(verbose_name='Почта клиента', unique=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя', help_text='Введите имя')
    second_name = models.CharField(max_length=50, verbose_name='Фамилия', help_text='Введите фамилию')
    third_name = models.CharField(max_length=50, verbose_name='Отчество', help_text='Введите отчество', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', help_text='Введите комментарий', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создал клиента", **NULLABLE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ("email",)
        permissions = [
            ("can_view_clients", "can view clients"),
            ("can_edit_is_active", "can edit active clients"),

            ("can_delete_clients", "can delete clients"),
        ]

    def __str__(self):
        return f"{self.email}"


class Message(models.Model):

    title = models.CharField(max_length=50, verbose_name='Заголовок сообщения', help_text='Введите заголовок сообщения')
    body = models.TextField(verbose_name='Содержание сообщения', help_text='Введите содержание сообщения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор сообщения", **NULLABLE)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ("title",)
        permissions = [
            ("can_change_message", "can change message"),
            ("can_delete_message", "can delete message"),
        ]

    def __str__(self):
        return f"{self.title}"


class Mailing(models.Model):

    client = models.ManyToManyField(Client, related_name='mailings', verbose_name='Клиент с почтой')
    message = models.ForeignKey(Message, related_name='mailings', verbose_name='Сообщение', on_delete=models.SET_NULL, **NULLABLE)
    send_date = models.DateField(**NULLABLE, verbose_name='Дата начала рассылки')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания рассылки')
    update_date = models.DateField(auto_now=True, verbose_name='Дата изменения рассылки')
    is_active = models.BooleanField(default=True)

    COMPLETED = "completed"
    CREATED = "created"
    STARTED = "started"
    DAY = "once a day"
    MINUTE = "once a minute"
    WEEK = "once a week"
    MONTH = "once a month"
    STATUS = [(COMPLETED, "completed"), (CREATED, "created"), (STARTED, "started")]
    INTERVAL = [
        (MINUTE, "once a minute"),
        (DAY, "once a days"),
        (WEEK, "once a week"),
        (MONTH, "once a months"),
    ]

    status = models.CharField(choices=STATUS, default=CREATED, verbose_name='Статус рассылки')
    interval = models.CharField(choices=INTERVAL, default=DAY, verbose_name='Интервал рассылки')
    end_date = models.DateTimeField(**NULLABLE, verbose_name="Дата окончания рассылки")
    # auto_start = models.BooleanField(default=True, verbose_name="Автоматический старт")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор рассылки", **NULLABLE)

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ("interval",)
        permissions = [
            ("can_view_mailing", "can view mailing"),
            ("can_edit_is_active", "can edit active mailing"),

            ("can_change_mailing", "can change mailing"),
            ("can_delete_mailing", "can delete mailing"),
            ("can_create_mailing", "can create mailing"),
        ]

        def __str__(self):
            return f"Рассылка {self.pk}"


class TryMailing(models.Model):
    SUCCESS = "success"
    FAIL = "fail"
    STATUSES = [(SUCCESS, "success"), (FAIL, "fail")]
    last_try = models.DateTimeField(auto_now_add=True, verbose_name="Дата последней попытки рассылки")
    status = models.CharField(choices=STATUSES, default=SUCCESS, verbose_name="Статус")
    response = models.TextField(**NULLABLE, verbose_name="Ответ")
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="Рассылка",
    )

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"
        ordering = ("status",)

    def __str__(self):
        return f"{self.status}"
