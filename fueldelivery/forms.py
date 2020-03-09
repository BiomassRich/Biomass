from django import forms
from . import models

class FuelLogDeliveryForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogDeliveryMod
        fields = ['delivery_ref_number','type_of_biomass','description_moisture_content','source_supplier',
        'quantity','BSL_Number','delivery_note_number','delivery_date']
