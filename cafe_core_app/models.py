from django.db import models

class Meal(models.Model):
    name = models.CharField('Название блюда', max_length=100)
    description = models.TextField('Описание блюда')
    price = models.IntegerField('Стоимость блюда')
    size = models.IntegerField('Грамовка блюда')

    class MealType(models.TextChoices):
        HOT_MEALS = 'Горячие блюда'
        DRINK = 'Напитки'
        DESSERT = 'Десерт'
        NO_TYPE = 'NO_TYPE'

    meal_type = models.CharField(
        max_length=30,
        choices=MealType.choices,
        default=MealType.NO_TYPE
    )
class MealClick(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING)
    click_date = models.DateTimeField('Дата клика')

class Users(models.Model):
    name = models.CharField('Name', max_length=100)

class Gallery(models.Model):
    image = models.ImageField(upload_to='static/img')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='images')