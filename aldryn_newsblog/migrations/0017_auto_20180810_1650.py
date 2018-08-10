# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-10 14:50
from __future__ import unicode_literals

import aldryn_categories.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_categories', '0004_auto_20150623_0859'),
        ('aldryn_newsblog', '0016_auto_20180329_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsblogarchiveplugin',
            name='category_config',
            field=aldryn_categories.fields.CategoryManyToManyField(blank=True, help_text='Will be applied if you do not use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting. If left empty, it will not use any filter on categories.', to='aldryn_categories.Category', verbose_name='Category configuration'),
        ),
        migrations.AddField(
            model_name='newsblogarchiveplugin',
            name='dynamic_category_config',
            field=models.BooleanField(default=False, verbose_name='Use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting instead of category configuration.'),
        ),
        migrations.AddField(
            model_name='newsblogarticlesearchplugin',
            name='category_config',
            field=aldryn_categories.fields.CategoryManyToManyField(blank=True, help_text='Will be applied if you do not use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting. If left empty, it will not use any filter on categories.', to='aldryn_categories.Category', verbose_name='Category configuration'),
        ),
        migrations.AddField(
            model_name='newsblogarticlesearchplugin',
            name='dynamic_category_config',
            field=models.BooleanField(default=False, verbose_name='Use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting instead of category configuration.'),
        ),
        migrations.AddField(
            model_name='newsblogauthorsplugin',
            name='category_config',
            field=aldryn_categories.fields.CategoryManyToManyField(blank=True, help_text='Will be applied if you do not use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting. If left empty, it will not use any filter on categories.', to='aldryn_categories.Category', verbose_name='Category configuration'),
        ),
        migrations.AddField(
            model_name='newsblogauthorsplugin',
            name='dynamic_category_config',
            field=models.BooleanField(default=False, verbose_name='Use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting instead of category configuration.'),
        ),
        migrations.AddField(
            model_name='newsblogcategoriesplugin',
            name='category_config',
            field=aldryn_categories.fields.CategoryManyToManyField(blank=True, help_text='Will be applied if you do not use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting. If left empty, it will not use any filter on categories.', to='aldryn_categories.Category', verbose_name='Category configuration'),
        ),
        migrations.AddField(
            model_name='newsblogcategoriesplugin',
            name='dynamic_category_config',
            field=models.BooleanField(default=False, verbose_name='Use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting instead of category configuration.'),
        ),
        migrations.AddField(
            model_name='newsblogfeaturedarticlesplugin',
            name='category_config',
            field=aldryn_categories.fields.CategoryManyToManyField(blank=True, help_text='Will be applied if you do not use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting. If left empty, it will not use any filter on categories.', to='aldryn_categories.Category', verbose_name='Category configuration'),
        ),
        migrations.AddField(
            model_name='newsblogfeaturedarticlesplugin',
            name='dynamic_category_config',
            field=models.BooleanField(default=False, verbose_name='Use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting instead of category configuration.'),
        ),
        migrations.AddField(
            model_name='newsbloglatestarticlesplugin',
            name='category_config',
            field=aldryn_categories.fields.CategoryManyToManyField(blank=True, help_text='Will be applied if you do not use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting. If left empty, it will not use any filter on categories.', to='aldryn_categories.Category', verbose_name='Category configuration'),
        ),
        migrations.AddField(
            model_name='newsbloglatestarticlesplugin',
            name='dynamic_category_config',
            field=models.BooleanField(default=False, verbose_name='Use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting instead of category configuration.'),
        ),
        migrations.AddField(
            model_name='newsblogtagsplugin',
            name='category_config',
            field=aldryn_categories.fields.CategoryManyToManyField(blank=True, help_text='Will be applied if you do not use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting. If left empty, it will not use any filter on categories.', to='aldryn_categories.Category', verbose_name='Category configuration'),
        ),
        migrations.AddField(
            model_name='newsblogtagsplugin',
            name='dynamic_category_config',
            field=models.BooleanField(default=False, verbose_name='Use the ALDRYN_NEWSBLOG_CATEGORIES_FROM_REQUEST setting instead of category configuration.'),
        ),
    ]
