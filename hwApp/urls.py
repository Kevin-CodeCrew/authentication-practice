from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # view all items
    path('all_items', views.all_items, name='all_items'),
    # view item by foreign key
    path('my_items', views.my_items, name='my_items'),
]
