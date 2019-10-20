from django import forms

from .models import Currency

class ConverterForm(forms.Form): #TODO make it a model form
    fromCurr = forms.ModelChoiceField(label='From', 
                                    queryset=Currency.objects.all(),
                                    empty_label="Select Currency")
    toCurr   = forms.ModelChoiceField(label='To', 
                                    queryset=Currency.objects.all(),
                                    empty_label="Select Currency")
    amount = forms.DecimalField(min_value = 0.1, initial=1)

    def convert(self):
        f = float(self.cleaned_data['fromCurr'].toBGN)
        t = float(self.cleaned_data['toCurr'].toBGN)
        s = float(self.cleaned_data['amount'])

        return round((s/t)*f, 4)

