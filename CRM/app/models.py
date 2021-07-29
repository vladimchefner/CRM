from django.db import models


class Client(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    is_subscribe = models.BooleanField('Подписка', default=False)
    chat_id = models.IntegerField('Чат id телеграма')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.surname


class Stuff(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    position = models.CharField('Должность', max_length=50)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.surname


class Order(models.Model):
    type = models.CharField('Тип заявки', max_length=50)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    stuff = models.ForeignKey('Stuff', on_delete=models.CASCADE)
    status = models.CharField('Статус', max_length=50)
    date = models.DateField('Дата')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.type
