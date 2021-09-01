from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.views.generic import CreateView, ListView


def detail_view(request, id):
    parts = get_object_or_404(SpareParts, id=id)
    return render(request, 'parts_detail.html', {'parts': parts})


def show_list(request):
    parts = SpareParts.objects.all()
    return render(request, 'parts_index.html', {'parts': parts})


def filter_ad(request, ad):
    parts = SpareParts.objects.filter(ad=ad)
    return render(request, 'spareparts/nov.html', {'parts': parts})


class AddPartsView(CreateView):
    model = SpareParts
    fields = ['ad', 'marka', 'sheher', 'shekil', 'qiymet', 'mezenne', 'info']

    def get_success_url(self):
        return reverse('index')
