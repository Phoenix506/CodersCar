from PIL.ImageChops import multiply
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import Avg, Max, Min, Sum
from django.contrib.auth.models import User
from django.conf import settings
from multiselectfield import MultiSelectField

Year = (
    ('1990', '1990'), ('1991', '1991'), ('1992', '1992'),
    ('1993', '1993'), ('1994', '1994'), ('1995', '1995'),
    ('1996', '1996'), ('1997', '1997'), ('1998', '1998'),
    ('1999', '1999'), ('2000', '2000'), ('2001', '2001'),
    ('2002', '2002'), ('2003', '2003'), ('2004', '2004'),
    ('2005', '2005'), ('2006', '2006'), ('2007', '2007'),
    ('2008', '2008'), ('2009', '2009'), ('2010', '2010'),
    ('2011', '2011'), ('2012', '2012'), ('2013', '2013'),
    ('2014', '2014'), ('2015', '2015'), ('2016', '2016'),
    ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    ('2020', '2020'), ('2021', '2021'),

)
currencies = (
    ('Azn ₼', 'Azn ₼'),
    ('Euro €', 'Euro €'),
    ('USD $', 'USD $'),

)
transmiss = (
    ('Mexaniki', 'Mexaniki'),
    ('Avtomat', 'Avtomat'),
    ('Robotlaşdırılmış', 'Robotlaşdırılmış'),
    ('Variator', 'Variator')
)
fueltype = (
    ('Benzin', 'Benzin'),
    ('Dizel', 'Dizel'),
    ('Qaz', 'Qaz'),
    ('Elektro', 'Elektro'),
    ('Hibrid', 'Hibrid'),

)

unit = (
    ('hyd', 'Hydraulic'),
    ('rot', 'Rotating DC '),
    ('ed', 'Eddy-Current')

)
MEDIA_CHOICES = [
    ('Audio', (
        ('vinyl', 'Vinyl'),
        ('cd', 'CD'),
    )
     ),
    ('Video', (
        ('vhs', 'VHS Tape'),
        ('dvd', 'DVD'),
    )
     ),
    ('unknown', 'Unknown'),
]

body = (
    ('Avtobus', 'Avtobus'),
    ('Buldozer', 'Buldozer'),
    ('İcma Maşını', 'İcma Maşını'),
    ('Skuter', 'Skuter'),
    ('ATV', 'ATV'),
    ('Qar avtomobili', 'Qar avtomobili'),
    ('SUV', 'SUV'),
    ('Ekskavator', 'Ekskavator'),
    ('Yük kranı', 'Yük kranı'),
    ('Yükləyici', 'Yükləyici'),
    ('Tikinti və yol', 'Tikinti və yol'),
    ('Kənd təsərrüfatı', 'Kənd təsərrüfatı'),
    ('Yarı qoşqu traktoru', 'Yarı qoşqu traktoru'),
    ('Yük maşını', 'Yük maşını'),
    ('Yüngül kommersiya', 'Yüngül kommersiya'),
    ('Qoşqu və yarı qoşqu', 'Qoşqu və yarı qoşqu'),
    ('Furqon', 'Furqon'),
    ('Hetçbek', 'Hetçbek'),
    ('Liftbek', 'Liftbek'),
    ('Kabriolet', 'Kabriolet'),
    ('Karvan', 'Karvan'),
    ('Kupe', 'Kupe'),
    ('Kvadrosikl', 'Kvadrosikl'),
    ('Mikroavtobus', 'Mikroavtobus'),
    ('Minivan', 'Minivan'),
    ('Motosiklet', 'Motosiklet'),
    ('Offroader / SUV', 'Offroader / SUV'),
    ('Pikap', 'Pikap'),
    ('Qolfkar', 'Qolfkar'),
    ('Rodster', 'Rodster'),
    ('Sedan', 'Sedan'),
    ('Universal', 'Universal'),
    ('Van', 'Van'),
    ('Yük maşını', 'Yük maşını'),

)

colors = (
    ('Qara', 'Qara'),
    ('Yaş Asfalt', 'Yaş Asfalt'),
    ('Boz', 'Boz'),
    ('Gümüşü', 'Gümüşü'),
    ('Ağ', 'Ağ'),
    ('Bej', 'Bej'),
    ('Tünd qırmızı', 'Tünd qırmızı'),
    ('Qırmızı', 'Qırmızı'),
    ('Çəhrayı', 'Çəhrayı'),
    ('Narıncı', 'Narıncı'),
    ('Qızılı', 'Qızılı'),
    ('Sarı', 'Sarı'),
    ('Yaşıl', 'Yaşıl'),
    ('Mavi', 'Mavi'),
    ('Göy', 'Göy'),
    ('Bənövşəyi', 'Bənövşəyi'),
    ('Qəhvəyi', 'Qəhvəyi'),
)

credi = (
    ('Kreditdədir', 'Kreditdədir'),
    ('Barter mümkündür', 'Barter mümkündür'),

)
supplies = (
    ('Yüngül lehimli disklər', 'Yüngül lehimli disklər'),
    ('Mərkəzi qapanma', 'Mərkəzi qapanma'),
    ('Dəri salon', 'Dəri salon'),
    ('Oturacaqların ventilyasiyası', 'Oturacaqların ventilyasiyas'),
    ('ABS', 'ABS'),
    ('Park radarı', 'Park radarı'),
    ('Ksenon lampalar', 'Ksenon lampalar'),
    ('Lyuk', 'Lyuk'),
    ('Arxa görüntü kamerası', 'Arxa görüntü kamerası'),
    ('Yağış sensoru', 'Yağış sensoru'),
    ('Oturacaqların isidilməsi', 'Oturacaqların isidilməsi'),
    ('Yan pərdələr', 'Yan pərdələr'),
)

city = (
    ('Baki', 'Bakı'),
    ('Gəncə', 'Gəncə'),
    ('Naxçıvan', 'Naxçıvan'),
    ('Xankəndi', 'Xankəndi'),
    ('Lənkəran', 'Lənkəran'),
    ('Mingəçevir', 'Mingəçevir'),
    ('Naftalan', 'Naftalan'),
    ('Sumqayıt', 'Sumqayıt'),
    ('Şəki', 'Şəki'),
    ('Şirvan', 'Şirvan'),
    ('Yevlax', 'Yevlax',),
    ('Abşeron', 'Abşeron',),
    ('Ağcabədi', 'Ağcabədi',),
    ('Ağdam', 'Ağdam',),
    ('Ağdaş', 'Ağdaş',),
    ('Ağstafa', 'Ağstafa',),
    ('Ağsu', 'Ağsu',),
    ('Astara', 'Astara',),
    ('Babək', 'Babək',),
    ('Beyləqan', 'Beyləqan',),
    ('Bərdə', 'Bərdə',),
    ('Biləsuvar', 'Biləsuvar',),
    ('Cəbrayıl', 'Cəbrayıl',),
    ('Cəlilabad', 'Cəlilabad',),
    ('Culfa', 'Culfa',),
    ('Daşkəsən', 'Daşkəsən',),
    ('Füzuli', 'Füzuli',),
    ('Gədəbəy', 'Gədəbəy',),
    ('Goranboy', 'Goranboy',),
    ('Göyçay', 'Göyçay',),
    ('Göygöl', 'Göygöl',),
    ('Hacıqabul', 'Hacıqabul',),
    ('Xaçmaz', 'Xaçmaz',),
    ('Xızı', 'Xızı',),
    ('Xocalı', 'Xocalı',),
    ('Xocavənd', 'Xocavənd',),
    ('İmişli', 'İmişli',),
    ('Kəlbəcər', 'Kəlbəcər',),
    ('Kürdəmir', 'Kürdəmir',),
    ('Qax', 'Qax',),
    ('Qazax', 'Qazax',),
    ('Qəbələ', 'Qəbələ',),
)


class Car(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    brand = models.CharField(max_length=100, verbose_name='Marka')
    model = models.CharField(max_length=50, verbose_name='Model')
    city = models.CharField(max_length=50, verbose_name='Şəhər', choices=city)
    engine = models.CharField(max_length=50, verbose_name="Mühərrik")
    body_type = models.CharField(max_length=50, choices=body, verbose_name='Ban Növü')
    transmission = models.CharField(max_length=50, choices=transmiss, verbose_name='Sürətlər qutusu')
    milage = models.PositiveIntegerField(default="0", verbose_name='Yürüş, km')
    color = models.CharField(max_length=50, choices=colors, verbose_name='Rəngi')
    fueltype = models.CharField(max_length=50, choices=fueltype, verbose_name='Yanacaq növü')
    year = models.CharField(max_length=50, choices=Year, verbose_name='Buraxılış ili')
    power = models.PositiveIntegerField(default="0", verbose_name='Mühərrikin gücü, a.g.')
    price = models.PositiveIntegerField(default="500", verbose_name='Qiyməti')
    currencie = models.CharField(max_length=10, choices=currencies, verbose_name='Məzənnə')
    credit = MultiSelectField(choices=credi, default="", verbose_name='', blank=True)
    info = models.TextField(max_length=400, default="", verbose_name='Əlavə Məlumat', blank=True)
    supply = MultiSelectField(choices=supplies, default="", verbose_name='Təchizat', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Əlavə olunma tarixi')
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    compare = models.ManyToManyField(User, related_name='compare', blank=True)
    phonenumber = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse("index")


class PostImage(models.Model):
    post = models.ForeignKey(Car, default=None, on_delete=models.CASCADE, related_name="images")
    image = models.FileField()

    def __str__(self):
        return self.post.brand
