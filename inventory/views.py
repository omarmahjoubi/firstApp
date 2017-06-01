from django.shortcuts import render
from django.http import Http404

from inventory.models import  Item

# Create your views here.

def index(request):
    items = Item.objects.exclude(amount=0)
    # function render create a HttpResponse that have a html file specified as second argument
    # and data passed as a dictionnary (third argument) where the key is the name of the variable in the html response
    return render(request,"inventory/index.html", { 'items' : items ,})

def item_detail(request,id):
    try :
        item = Item.objects.get(id=id)
    except Item.DoesNotExist :          # if objects.get return nothing
        raise Http404("this Item does not exist")
    return render(request,'inventory/item_detail.html',{ 'item' : item ,})