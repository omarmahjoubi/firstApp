from django.contrib import admin

#password superuser : rootroot
from .models import Item

class ItemAdmin(admin.ModelAdmin):  #Defin how the admin will be displayes in the admin item page
    list_display = ['title', 'amount']   #the attribute that will be shown in the admin items page


admin.site.register(Item,ItemAdmin)   #add ItemAdmin as a scond argument to make it effective
