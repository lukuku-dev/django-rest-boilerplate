from django.db.models.fields.reverse_related import ForeignObjectRel
from django.db.models.fields.reverse_related import OneToOneRel
from django.db.models.fields.reverse_related import ManyToOneRel
from django.contrib import admin
from django.db import models


class AutoCompleteAdminMixin:
    autocomplete_fields = ()

    def __init__(self, model, admin_site, *args, **kwargs):
        self.autocomplete_fields = self.setup_autocomplete_fields(model)
        self.raw_id_fields = self.setup_raw_id_fields(model)
        super().__init__(model, admin_site, *args, **kwargs)

    def setup_autocomplete_fields(self, model):
        return tuple(f.name for f in model._meta.get_fields()
                     if isinstance(f, models.ForeignKey)
                     or isinstance(f, models.OneToOneField))

    def setup_raw_id_fields(self, model):
        return tuple(f.name for f in model._meta.get_fields()
                     if isinstance(f, models.ManyToManyField))


class ModelAdmin(admin.ModelAdmin):

    @staticmethod
    def check_related_field(field):
        return isinstance(field, (ForeignObjectRel, ManyToOneRel, OneToOneRel))

    def get_list_display(self, request):
        list_display = self.list_display

        if list_display == ('__str__', ):
            list_display = [field.name for field in self.model._meta.get_fields() if not self.check_related_field(field)]
            for field_name in ['created', 'modified']:
                if field_name in list_display:
                    list_display.remove(field_name)
                    list_display.append(field_name)

        if hasattr(self, 'additional_list_display'):
            list_display.extend(self.additional_list_display)
        
        exclude_list_display = getattr(self, 'exclude_list_display', ())
        list_display = [field for field in list_display if field not in exclude_list_display]

        return list_display
