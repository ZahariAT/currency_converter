from django.contrib import admin

from .models import Currency
from .management.commands.loadBNB import Command

# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    actions = ['sync_bnb']
    list_display = ['name', 'toBGN', 'amount', 'fromBGN']
    fields = ('name', 'toBGN', 'amount') #exlude = [fromBGN]

    def sync_bnb(self, request, queryset): #TODO not select an object to trigger action
        response = Command().handle()      #(interesting oppinion I read on why one must select an item first)This is an intentional design decision. Actions that don't act on specific items are a fundamentally different and representing them in the same UI is bad practice. You can add links to the object-tools portion of the page to have non-item specific actions.
        if response == None:
            self.message_user( request, f'{request} was successful!')
        else:
            self.message_user( request, f'{request} was not successful bacause {response}!')

    sync_bnb.short_description = 'Sync with BNB'


#Allow for Admin Actions to be applied to an empty QuerySet
#This is an intentional design decision. Actions that don't act on specific items are a fundamentally different and representing them in the same UI is bad practice. You can add links to the object-tools portion of the page to have non-item specific actions.
admin.site.register(Currency, CurrencyAdmin)
