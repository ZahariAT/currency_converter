from django.urls import path
from .views import CurrencyListView#, calculator_view


app_name = 'currency'
urlpatterns = [
    path('', CurrencyListView.as_view())#,
    #path('', calculator_view),
]
