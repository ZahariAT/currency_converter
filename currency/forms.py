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
        f_a = float(self.cleaned_data['fromCurr'].amount)
        t = float(self.cleaned_data['toCurr'].toBGN)
        t_a = float(self.cleaned_data['toCurr'].amount)
        a = float(self.cleaned_data['amount'])
        f = f/f_a
        t = t/t_a

        return round((a/t)*f, 4)

