# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(default=b'', max_length=254)),
                ('company', models.CharField(default=b'', max_length=254, null=True, blank=True)),
                ('phone', models.CharField(default=b'', max_length=254)),
                ('note', models.TextField(default=b'')),
                ('newsletter', models.BooleanField(default=True, verbose_name=b'newsletter')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
