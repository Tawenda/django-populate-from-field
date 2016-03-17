# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _
from django.db import models
from populate_from_field.exceptions import UnkownPopulateFromSource


class BasePopulateFromField(models.Field):

    description = _("Field that populate from callable or instance attribut")

    def __init__(self, populate_from=None, fallback_on_default = True, *args, **kwargs):

        self.fallback_on_default = fallback_on_default

        if isinstance(populate_from, basestring):
            self.populate_from = lambda instance: self._value_from_field(instance, populate_from)
        elif callable(populate_from):
            self.populate_from = populate_from
        else:
            self.populate_from = None
        super(BasePopulateFromField, self).__init__(*args, **kwargs)

    def _value_from_field(self,instance, populate_from):
        if hasattr(instance, populate_from):
            return getattr(instance, populate_from)
        elif self.fallback_on_default:
            return self.get_default()
        else:
            raise UnkownPopulateFromSource('Instance hasn\'t attr %s' % populate_from)

    def deconstruct(self):
        name, path, args, kwargs = super(BasePopulateFromField, self).deconstruct()
        kwargs['populate_from'] = self.populate_from
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):

        current_field_value = self._get_val_from_obj(model_instance)

        if current_field_value == self.get_default() or not self.editable:

            if self.populate_from is not None:
                value = self.populate_from(model_instance)
            else:
                value = self._value_from_field(model_instance, 'populate_%s' % self.attname)
                if callable(value):
                    value = value()

            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(BasePopulateFromField, self).pre_save(model_instance, add)


