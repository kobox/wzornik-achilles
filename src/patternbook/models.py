# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField('Imię i Nazwisko', max_length=254, default='', blank=False, null=False)
    company = models.CharField('Firma', max_length=254, default='', blank=True, null=True)
    phone = models.CharField('Telefon', max_length=254, default='')
    note = models.TextField('Uwagi', default='', blank=True, null=True)
    newsletter = models.BooleanField('Newsletter', default=True, help_text='Chcę być informowany o nowościach i ofertach firmy Achilles.')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email
