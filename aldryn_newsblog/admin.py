from django.contrib import admin
from cms.admin.placeholderadmin import FrontendEditableAdmin
from parler.admin import TranslatableAdmin

from aldryn_apphooks_config.admin import BaseAppHookConfig
from aldryn_people.models import Person

from .versioning import VersionedPlaceholderAdminMixin
from . import models


class ArticleAdmin(VersionedPlaceholderAdminMixin,
                   TranslatableAdmin,
                   FrontendEditableAdmin):
    # TODO: make possible to edit placeholder

    def add_view(self, request, *args, **kwargs):
        data = request.GET.copy()
        try:
            person = Person.objects.get(user=request.user)
            data['author'] = person.pk
            request.GET = data
        except Person.DoesNotExist:
            pass
        return super(ArticleAdmin, self).add_view(request, *args, **kwargs)

admin.site.register(models.Article, ArticleAdmin)


class NewsBlogConfigAdmin(BaseAppHookConfig):
    def get_config_fields(self):
        return []

admin.site.register(models.NewsBlogConfig, NewsBlogConfigAdmin)
