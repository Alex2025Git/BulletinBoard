from django.db import models

from config.settings import AUTH_USER_MODEL


# def datepublished(date):
#     """
#     Функция для преобразования даты в удобочитаемый вид
#     :param date: "DateTimeField"
#     :return: "DateTimeField"
#     """
#     return date.strftime('%d.%m.%Y')


class Ads(models.Model):
    """
    Модель объявления
    """

    title = models.CharField(
        max_length=100,
        verbose_name="Наименование товара",
        help_text="Укажите наименование товара",
        blank=True,
        null=True,
    )
    price = models.IntegerField(
        verbose_name="Цена на товар",
        help_text="Укажите цену на товар",
        blank=True,
        null=True,
        default = 0
    )
    description = models.TextField(
        verbose_name="Описание товара",
        help_text="Опишите товар",
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания объявления",
        help_text="Укажите дату",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        """
        Строковое отображение объекта
        """
        return f'{self.title}-{self.price} руб., объявление добавлено - {self.created_at}г.'

# Модель объявления должна содержать следующие поля:
#
# - title — название товара.
# - price — цена товара (целое число).
# - description — описание товара.
# - author — пользователь, который создал объявление.
# - created_at — время и дата создания объявления.
# - Объявления должны быть отсортированы по дате создания (чем новее, тем выше).


class Feedback(models.Model):
    """
    Модель отзыва
    """
    text = models.TextField(
        verbose_name="Текст отзыва",
        help_text="Оставьте свой отзыв",
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        blank=True,
        null=True
    )
    ad = models.ForeignKey(
        Ads,
        on_delete=models.CASCADE,
        verbose_name='Объявление',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания отзыва",
        help_text="Укажите дату",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.ad} ({self.author}, дата отзыва - {self.created_at})"

