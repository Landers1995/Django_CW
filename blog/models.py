from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=35, verbose_name='Заголовок', help_text='Введите заголовок')
    body = models.TextField(verbose_name='Текст', help_text='Введите текст статьи')
    image = models.ImageField(upload_to="product/photo", blank=True, null=True, verbose_name="Изображение", help_text="Загрузите превью статьи")
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата написания статьи",
        help_text="Укажите дату написания статьи",)
    count_views = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров статьи",
    )
    is_publication = models.BooleanField(
        verbose_name="Опубликовать?",
        default=True
    )
