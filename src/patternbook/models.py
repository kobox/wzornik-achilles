from django.db import models

# Create your models here.


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=254, default='', blank=False, null=False)
    company = models.CharField(max_length=254, default='', blank=True, null=True)
    phone = models.CharField(max_length=254, default='')
    note = models.TextField(default='', blank=True, null=True)
    newsletter = models.BooleanField("newsletter", default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email
