from django.db import models
from django.urls import reverse
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name="Тури")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тури"
        verbose_name_plural = "Тури"


class Handler(models.Model):
    name = models.CharField(max_length=200, verbose_name="Маъсул ҳодим ФИО")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Маъсул ҳодим"
        verbose_name_plural = "Маъсул ҳодимлар"


class Structure(models.Model):
    name = models.CharField(max_length=200, verbose_name="Маъсул бўлим номи")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Маъсул бўлим"
        verbose_name_plural = "Маъсул бўлимлар"


class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name="Сотувчи корхона номи")
    contact = models.CharField(max_length=200, verbose_name="Сотувчи корхона контакти")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотувчи корхона"
        verbose_name_plural = "Сотувчи корхоналар"


class Device(models.Model):
    name = models.CharField(max_length=200, verbose_name="номи")
    type = models.ForeignKey(
        Type, verbose_name="тури",
        on_delete=models.CASCADE
    )
    description = models.TextField(verbose_name="Маълумот")
    inventar = models.IntegerField(verbose_name="Инвентар рақами")
    company = models.ForeignKey(
        Company,
        verbose_name="Сотувчи корхона",
        on_delete=models.CASCADE
    )
    price = models.IntegerField(verbose_name="нархи")
    bought = models.DateField(verbose_name="сана", blank=True, null=True)
    guarranty = models.IntegerField(verbose_name="кафолат муддати")
    structure = models.ForeignKey(
        Structure,
        verbose_name="Маъсул бўлим",
        on_delete=models.CASCADE
    )
    handler = models.ForeignKey(
        Handler,
        verbose_name="Маъсул ходим",
        on_delete=models.CASCADE
    )
    document = models.FileField(upload_to='documents/', verbose_name="Хужжат юклаш (Шартнома, чек ва ҳ.к)", blank=True)
    service = models.CharField(max_length=200, verbose_name="Техник холати, хизмат кўрсатиш, алохида холатлар",)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    url = models.SlugField(max_length=160, unique=True, null=True, verbose_name="Инв номер")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(f'https://e-invertar-af5c0e74380e.herokuapp.com/devices/{self.url}')
        canvas = Image.new('RGB', (375, 375), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}-{self.url}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('device_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Инвентаризация"
        verbose_name_plural = "Инвентаризация"


