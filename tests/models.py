# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models

from populate_from_field.fields import PopulateFromCharField


class UnknownCharFieldTestModel(models.Model):
    source_text = models.CharField(max_length=256)
    target_text = PopulateFromCharField(populate_from='text_populate_from', max_length=256)


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
    target_text = PopulateFromCharField(max_length=256)