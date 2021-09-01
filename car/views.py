from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Car, PostImage
from .forms import SellingForm
from django.views.generic import CreateView, ListView
from django.contrib import messages
from .filters import CarFilter
from django.core.paginator import Paginator, EmptyPage
from django.core.mail import send_mail
from django.db.models import Q


def show_all_car_page(request):
    filtered_cars = CarFilter(
        request.GET,
        queryset=Car.objects.all()
    )

    paginator = Paginator(filtered_cars.qs, 6)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    photos = PostImage.objects.all()
    car = Car.objects.first()
    favourite = car.favourite.through.objects.filter(user_id=request.user.id)
    list_a = []
    for i in favourite:
        list_a.append(i.car_id)
    compare = car.compare.through.objects.filter(user_id=request.user.id)
    list_b = []
    for j in compare:
        list_b.append(j.car_id)

    context = {
        'filtered_cars': filtered_cars,
        'posts': posts,
        'photos': photos,
        'favourite': list_a,
        'compare': list_b
    }

    return render(request, 'index.html', context=context)


def my_announcement(request):
    post = Car.objects.filter(author=request.user)
    photos = PostImage.objects.all()
    context = {
        'post': post,
        'photos': photos
    }
    return render(request, 'my_announcement.html', context)


def milage(request):
    post = Car.objects.order_by('milage')
    photos = PostImage.objects.all()
    context = {
        'post': post,
        'photos': photos
    }
    return render(request, 'milage.html', context)


def year(request):
    post = Car.objects.order_by('-year')
    photos = PostImage.objects.all()
    context = {
        'post': post,
        'photos': photos
    }
    return render(request, 'year.html', context)


def search_cars(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cars = Car.objects.filter(Q(brand__contains=searched) | Q(model__contains=searched))
        photos = PostImage.objects.all()

        return render(request,
                      'search_cars.html',
                      {'searched': searched,
                       'cars': cars,
                       'photos': photos})
    else:
        return render(request,
                      'search_cars.html',
                      {})


def detail_view(request, id):
    post = get_object_or_404(Car, id=id)
    photos = PostImage.objects.filter(post=post)

    return render(request, 'detail.html', {'post': post, 'photos': photos})


def credit_view(request):
    return render(request, 'credit.html')


def insure_view(request):
    return render(request, 'insure.html')


def contact_view(request):
    if request.method == "POST":
        message_fullname = request.POST['message_fullname']
        message_email = request.POST['message_email']
        message = request.POST['message']

        # Send an email
        send_mail(
            message_fullname + '- dən Email',
            message,
            message_email,
            ['oyunlarucun1@gmail.com'],
        )
        return render(request, 'contact.html', {'message_fullname': message_fullname})
    else:
        return render(request, 'contact.html')


def selling_view(request):
    return render(request, 'selling.html')


def filter_city(request, city):
    post = Car.objects.all()
    cities = post.filter(city=city)
    photos = PostImage.objects.all()
    return render(request, 'city.html',
                  {'cities': cities,
                   'photos': photos
                   }
                  )


def filter_type(request, body_type):
    post = Car.objects.all()
    body_types = post.filter(body_type=body_type)
    photos = PostImage.objects.all()
    return render(request, 'body_type.html',
                  {'body_types': body_types,
                   'photos': photos}
                  )


def filter_minik(request):
    post = Car.objects.all()
    photos = PostImage.objects.all()
    minik = post.filter(
        body_type__in=["Sedan", "SUV", "Hetçbek", "Liftbek", "Universal", "Minivan", "Kupe", "Pikap", "Kabriolet",
                       "Furqon"])
    return render(request, 'passenger.html', {'minik': minik,
                                              'photos': photos
                                              })


def filter_ticari(request):
    post = Car.objects.all()
    photos = PostImage.objects.all()
    commercial = post.filter(
        body_type__in=["Yüngül kommersiya", "Yük maşını", "Yarı qoşqu traktoru", "Avtobus", "Qoşqu və yarı qoşqu",
                       "Kənd təsərrüfatı", "Tikinti və yol", "Yükləyici", "Yük kranı",
                       "Ekskavator", "Buldozer", "İcma Maşını"])
    return render(request, 'commercial.html', {'commercial': commercial,
                                               'photos': photos
                                               })


def filter_moto(request):
    post = Car.objects.all()
    photos = PostImage.objects.all()
    moto = post.filter(
        body_type__in=["Motosiklet", "Skuter", "ATV", "Qar avtomobili", ])
    return render(request, 'moto.html', {'moto': moto,
                                         'photos': photos
                                         })


def post_favourite_list(request):
    user = request.user
    favourite_posts = user.favourite.all()
    photos = PostImage.objects.all()

    context = {
        'favourite_posts': favourite_posts,
        'photos': photos
    }
    return render(request, 'favourites.html', context)


@login_required
def favourite_post(request, id):
    post = get_object_or_404(Car, id=id)

    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())


def post_compare_list(request):
    user = request.user
    compare_posts = user.compare.all()
    photos = PostImage.objects.all()

    context = {
        'compare_posts': compare_posts,
        'photos': photos
    }
    return render(request, 'compares.html', context)


def compare_post(request, id):
    post = get_object_or_404(Car, id=id)
    if post.compare.filter(id=request.user.id).exists():
        post.compare.remove(request.user)
    else:
        post.compare.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())

@login_required(login_url='/user/login')
def AddCarView(request):
    form = SellingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        a = form.save(commit=False)
        a.author = request.user
        a.save()
        img = request.FILES.getlist('images')
        for i in img:
            PostImage.objects.create(
                image=i,
                post=a
            )
        return redirect('index')
    context = {'form': form}
    return render(request, 'car/car_form.html', context)
