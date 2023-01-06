from django.shortcuts import render
from .models import Meal, MealClick, Users, Gallery
from django.utils import timezone
import os

from matplotlib import pylab
from pylab import *

import jwt
from users.models import User

def menu(request):
    meal_categories = list(filter(lambda el: 'NO_TYPE' not in el[0], Meal.MealType.choices))
    return render(request, 'menu.html', {'meal_categories': meal_categories})

def meal_category(request, meal_category):
    meals_by_category = Meal.objects.filter(meal_type=meal_category)
    return render(request, 'meals.html', {'meals': meals_by_category, 'meal_category': meal_category})

def meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    meal.mealclick_set.create(click_date=timezone.now())
    img = Gallery.objects.filter(meal=meal)

    token = request.COOKIES.get('jwt')
    if token is not None:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        user = User.objects.filter(id=payload['id']).first()
        Users.objects.create(name=user.username)

    else:
        user = 'anonim'
        Users.objects.create(name=user)

    return render(request, 'meal.html', {'meal': meal, 'img': img})

def meal_statistics(request):
    click = MealClick.objects.all()
    users = Users.objects.all()

    def funk(param, click=None, users=None):
        food = []
        if click is not None:
            for i in click:
                food.append(i.meal.name)
        if users is not None:
            for i in users:
                food.append(i.name)

        pes = {}
        pes_ = {}
        for name in food:
            pes[name] = pes.get(name, 0) + 1
        for i, x in sorted(sorted(pes.items()), key=lambda x: x[1], reverse=True):
            if not len(pes_) == param:
                pes_[i] = pes_.get(i, x)
        return pes_
    pes_ = funk(3, click=click)
    res_ = funk(10, users=users)


    context = {
        # 'value': click,
        # 'users': users,
        'res': res_,
        'meal': pes_,
    }
    return render(request, 'meal_statistics.html', context=context)

matplotlib.use('Agg')
def GraphsViewBar(request,meal_id):
    namb = 0
    x = []
    y = []
    meal = Meal.objects.get(id=meal_id)

    for i in meal.mealclick_set.all():
        namb += 1
        x.append(namb)
        y.append(i.click_date.strftime("%d-%m-%y"))
    fig = plt.figure()
    plt.plot(y, x)
    plt.ylabel(meal.name)
    plt.xlabel('Дата')
    os.remove("cafe_core_app/static/img/core.png")
    fig.savefig('cafe_core_app/static/img/core.png')
    addr = 'img/core.png'
    plt.close(fig)
    return render(request, 'grafic.html', {'addr': addr})

