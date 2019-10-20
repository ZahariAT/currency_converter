from django import forms

from .models import Currency

class ConverterForm(forms.Form):
    fromCurr = forms.ModelChoiceField(label='From', 
                                    queryset=Currency.objects.all(),
                                    empty_label="Select Currency")
    toCurr   = forms.ModelChoiceField(label='To', 
                                    queryset=Currency.objects.all(),
                                    empty_label="Select Currency")
    sum = forms.DecimalField(min_value = 0.1, initial=1)

    def convert(self):
        f = float(self.cleaned_data['fromCurr'].toBGN)
        t = float(self.cleaned_data['toCurr'].toBGN)
        s = float(self.cleaned_data['sum'])

        return round((s/t)*f, 2)

