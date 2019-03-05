from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ItemModel


# render welcome page
def index(request):
    return render(request, 'hwApp/index.html')


# render all items from model after login at welcome page
@login_required
def all_items(request):
    items_all = ItemModel.objects.all()
    context = {
        'items_all': items_all
    }
    return render(request, 'hwApp/all_items.html', context)


# render items by foreign key from link on all_items
@login_required
def my_items(request):
    item_fk = ItemModel.objects.filter(item_fk=request.user)
    context = {
        'item_fk': item_fk
    }
    return render(request, 'hwApp/my_items.html', context)
