from django.shortcuts import render
from django.views import View

from .models import Currency
from .forms import ConverterForm

# Create your views here.

class CurrencyListView(View):
    template_name = 'currency_list.html'
    queryset = Currency.objects.all()

    def get(self, request, *args,**kwargs):
        form = ConverterForm()
        context = {
            'form': form,
            'object_list': self.queryset
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *args,**kwargs):
        result = None
        form = ConverterForm(request.POST)
        if form.is_valid():
            result = form.convert()
            #form = ConverterForm()
        context = {
            'form': form,
            'result': result,
            'object_list': self.queryset
        }
        return render(request, self.template_name, context)
