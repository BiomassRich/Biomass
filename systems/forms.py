from django import forms
from . import models

class AddFuelLogOneForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemOneMod
        fields = ['buckets_added']

class MonthlyMeterOneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterOneForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemOneMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']

class AddFuelLogTwoForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemTwoMod
        fields = ['buckets_added']

class MonthlyMeterTwoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterTwoForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemTwoMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']

class AddFuelLogThreeForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemThreeMod
        fields = ['buckets_added']

class MonthlyMeterThreeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterThreeForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemThreeMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']

class AddFuelLogFourForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemFourMod
        fields = ['buckets_added']

class MonthlyMeterFourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterFourForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemFourMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']

class AddFuelLogFiveForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemFiveMod
        fields = ['buckets_added']

class MonthlyMeterFiveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterFiveForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemFiveMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']

class AddFuelLogSixForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemSixMod
        fields = ['buckets_added']

class MonthlyMeterSixForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterSixForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemSixMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']

class AddFuelLogSevenForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemSevenMod
        fields = ['buckets_added']

class MonthlyMeterSevenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterSevenForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemSevenMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']

class AddFuelLogEightForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemEightMod
        fields = ['buckets_added']

class MonthlyMeterEightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterEightForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemEightMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']

class AddFuelLogNineForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemNineMod
        fields = ['buckets_added']

class MonthlyMeterNineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterNineForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemNineMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']

class AddFuelLogTenForm(forms.ModelForm):
    class Meta:
        model = models.FuelLogSystemTenMod
        fields = ['buckets_added']

class MonthlyMeterTenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MonthlyMeterTenForm, self).__init__(*args, **kwargs)
       self.fields['system'].widget.attrs['readonly'] = True
       self.fields['serial_number'].widget.attrs['readonly'] = True
       self.fields['previous_meter_reading'].widget.attrs['readonly'] = True

    class Meta:
        model = models.monthlyMeterSystemTenMod
        fields = ['system', 'serial_number','current_meter_reading','previous_meter_reading','notes']
