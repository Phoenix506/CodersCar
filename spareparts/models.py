from django.db import models

currencies = (
    ('Azn ₼', 'Azn ₼'),
    ('Euro €', 'Euro €'),
    ('USD $', 'USD $'),
)
parts = (
    ('Təkərlər və disklər','Təkərlər və disklər'),
    ('Yağlar və avtomobil kimyəvi maddələr', 'Yağlar və avtomobil kimyəvi maddələr'),
    ('Akkumlyatorlar', 'Akkumlyatorlar'),
    ('Bədən hissələri', 'Bədən hissələri'),
    ('Elektrik və işıq', 'Elektrik və işıq'),
    ('Mühərrik və alovlanma sistemi', 'Mühərrik və alovlanma sistemi'),
    ('Aksesuarlar', 'Aksesuarlar'),
    ('Alətlər', 'Alətlər'),

)


class SpareParts(models.Model):
    ad = models.CharField(max_length=120, choices=parts, verbose_name='Növü')
    marka = models.CharField(max_length=50, verbose_name="Markası")
    qiymet = models.PositiveIntegerField(default="0", verbose_name='Qiyməti')
    sheher = models.CharField(max_length=50, verbose_name='Şəhər')
    mezenne = models.CharField(max_length=10, choices=currencies, default='', verbose_name='Məzənnə')
    shekil = models.FileField(null=True, verbose_name='Shekil elave et:')
    info = models.TextField(max_length=400, default="", verbose_name='Əlavə Məlumat', blank=True)

    def __str__(self):
        return self.ad
