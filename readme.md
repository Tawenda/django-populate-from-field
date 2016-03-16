A field mixin that allow your to define custom fields that populate from severals sources

## Installation

Last release is 1.1

    pip install <git url>

## Usage

```python
    
    # Define your own fields
    from populate_from_field.fields import BasePopulateFromField
    from django.db.models import CharField
    
    class MyCharField(BasePopulateFromField, CharField):
        pass
    
    class MyModel(modles.Model):
        
        def custom_populate_from(self):
            return "Plop"
        
        # will populate from self.custom_populate_from if its value is not set explicitly
        field1 = MyCharField(populate_from=custom_populate_from, max_length=255)
        
        # because of editale=False, will ALWAYS populate from self.custom_populate_from 
        field2 = MyCharField(populate_from=custom_populate_from, , max_length=255, editable=False)
    
        source = models.CharField(max_length=255)
        
        # populate from source attribute 
        field3 = MyCharField(populate_from='source', max_length=255)
        
        # if populate_from is omitted, the field will try to populate from instance.populate_<fieldname> method
        field4 = MyCharField(max_length=255)
        def populate_field4(self):
            return "I like plop"
        
```
