# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models

from .fields import PopulateFromCharField, PopulateFromBooleanField


class UnknownCharFieldTestModel(models.Model):
    source_text = models.CharField(max_length=256)
    target_text = PopulateFromCharField(populate_from='text_populate_from', fallback_on_default=False, max_length=256)


class CharFieldTestModel(models.Model):
    source_text = models.CharField(max_length=256)
    target_text = PopulateFromCharField(populate_from='source_text', max_length=256)


class FnCharFieldTestModel(models.Model):
    def populate_from(self):
        return "%s--" % self.source_text

    source_text = models.CharField(max_length=256)
    target_text = PopulateFromCharField(populate_from=populate_from, max_length=256)


class NonEditableCharFieldTestModel(models.Model):
    source_text = models.CharField(max_length=256)
    target_text = PopulateFromCharField(populate_from='source_text', max_length=256, editable=False)


class AutoPopulateFormCharFieldTestModel(models.Model):
    source_text = models.CharField(max_length=256)
    target_text = PopulateFromCharField(max_length=256)

    def populate_target_text(self):
        return "%s--" % self.source_text


class notImplementedAutoPopulateFormCharFieldTestModel(models.Model):
    source_text = models.CharField(max_length=256)
    target_text = PopulateFromCharField(max_length=256, fallback_on_default=False)

class DefaultFallbackAutoPopulateFormCharFieldTestModel(models.Model):
    target_text = PopulateFromCharField(max_length=256, default='plop')


class TestBooleanFieldModel(models.Model):
    def populate_from(self):
        return False

    field = PopulateFromBooleanField(populate_from=populate_from, default=None)
