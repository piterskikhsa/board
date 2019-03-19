from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']

    def __str__(self):
        return f'{self.title} - {self.price}'


class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name
