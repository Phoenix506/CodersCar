from car.models import Car
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def fav_view(request):
    car = Car.objects.first()
    favourite = car.favourite.through.objects.filter(user_id=request.user.id)
    list_a = []
    for i in favourite:
        list_a.append(i.car_id)

    return list_a


def comp_view(request):
    car = Car.objects.first()
    compare = car.compare.through.objects.filter(user_id=request.user.id)
    list_b = []
    for j in compare:
        list_b.append(j.car_id)

    return list_b