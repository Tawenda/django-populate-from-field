# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.test import TestCase

from populate_from_field.exceptions import UnkownPopulateFromSource
from .models import (UnknownCharFieldTestModel, CharFieldTestModel, FnCharFieldTestModel, NonEditableCharFieldTestModel,
                     AutoPopulateFormCharFieldTestModel, notImplementedAutoPopulateFormCharFieldTestModel)


class PopulateFromFieldTest(TestCase):
    def test_populate_from_field_with_non_existent_source(self):
        source_text = 'test_populate_from_field_with_non_existent_source'
        instance = UnknownCharFieldTestModel(source_text=source_text)
        self.assertRaises(UnkownPopulateFromSource, instance.save)

    def test_populate_from_field(self):
        source_text = 'test_populate_from_field'
        instance = CharFieldTestModel(source_text=source_text)
        instance.save()
        self.assertEqual(source_text, instance.source_text)
        self.assertEqual(source_text, instance.target_text)

    def test_populate_from_field_with_fn(self):
        source_text = 'test_populate_from_field_with_fn'
        instance = FnCharFieldTestModel(source_text=source_text)
        instance.save()
        self.assertEqual(source_text, instance.source_text)
        self.assertEqual("%s--" % source_text, instance.target_text)

    def test_populate_from_field_editable(self):
        source_text = 'test_populate_from_field_editable'
        instance = CharFieldTestModel(source_text=source_text, target_text='target')
        instance.save()
        self.assertEqual(source_text, instance.source_text)
        self.assertEqual('target', instance.target_text)

    def test_populate_from_field_non_editable(self):
        source_text = 'test_populate_from_field_non_editable'
        instance = NonEditableCharFieldTestModel(source_text=source_text, target_text='target')
        instance.save()
        self.assertEqual(source_text, instance.source_text)
        self.assertEqual(source_text, instance.target_text)

    def test_auto_populate(self):
        source_text = 'test_auto_populate'
        instance = AutoPopulateFormCharFieldTestModel(source_text=source_text)
        instance.save()
        self.assertEqual(source_text, instance.source_text)
        self.assertEqual(instance.populate_target_text(), instance.target_text)

    def test_not_implemented_auto_populate(self):
        source_text = 'test_not_implemented_auto_populate'
        instance = notImplementedAutoPopulateFormCharFieldTestModel(source_text=source_text)
        self.assertRaises(UnkownPopulateFromSource, instance.save)
