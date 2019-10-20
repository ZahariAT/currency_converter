import requests

from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from currency.models import Currency

class Command(BaseCommand):
    help = 'Extracts currencies from BNB'
    URL = "http://bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm"

    def handle(self, *args, **options):
        Currency.objects.all().delete() #TODO update objects instead deleting and creating
        response = self._helper()

        return response

    def _helper(self):
        try:
            response = requests.get(self.URL)
            response.raise_for_status()
        except HTTPError as http_err:
            return f'HTTP error occurred: {http_err}'
        except Exception as err:
            return f'Other error occurred: {err}'

        if response.status_code != 200:
            return f'Expected status code 200, but got {response.status_code}'

        soup = BeautifulSoup(response.content, 'lxml') 
        tr_list = soup.find_all('tr')

        if len(tr_list) == 0:
            return'Content not found!'

        for tr in tr_list[1:-1]:
            td_list = tr.find_all('td')
           # Currency(**{k:td.text for td in td_list[1:4] for k in ('name', 'amount' 'toBGN')}).save()
            Currency(name=td_list[1].text, toBGN=td_list[3].text, amount=td_list[2].text).save()

        print('Done!')