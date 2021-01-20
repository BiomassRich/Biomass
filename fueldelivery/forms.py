from django import forms
from . import models

class FuelLogDeliveryForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogDeliveryMod
        fields = ['delivery_ref_number','type_of_biomass','description_moisture_content','source_supplier',
        'quantity','BSL_Number','delivery_note_number','delivery_date']
        widgets = {
          'delivery_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

        def __init__(self, *args, **kwargs):
            super(FuelLogDeliveryForm, self).__init__(*args, **kwargs)
            # input_formats to parse HTML5 datetime-local input to datetime field
            self.fields['delivery_date'].input_formats = ['%Y-%m-%dT%H:%M']
