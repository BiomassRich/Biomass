from django import forms
from . import models

class ReportDateForm(forms.ModelForm):
    fromdate = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    todate = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    def __init__(self, *args, **kwargs):
       super(ReportDateForm, self).__init__(*args, **kwargs)
       self.fields['fromdate'].label = "From Date"
       self.fields['todate'].label = "To Date"

    class Meta:
        model = models.DatesMod
        fields = ['fromdate','todate']
