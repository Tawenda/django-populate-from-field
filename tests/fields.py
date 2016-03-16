# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from populate_from_field.fields import BasePopulateFromField
from django.db.models import CharField, BooleanField


class PopulateFromCharField(BasePopulateFromField, CharField):
    pass


class PopulateFromBooleanField(BasePopulateFromField, BooleanField):
    pass
