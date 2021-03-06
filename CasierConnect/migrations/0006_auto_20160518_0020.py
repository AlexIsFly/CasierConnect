# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CasierConnect', '0005_casier_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='casier',
            name='email',
            field=models.EmailField(default='pubox.ag@gmail.com', help_text="L'email de confirmation sera envoyé à cette adresse, également utilisé comme identifiant.", max_length=254, verbose_name='Courriel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='casier',
            name='pseudo',
            field=models.CharField(default='Sudo', max_length=20),
            preserve_default=False,
        ),
    ]
