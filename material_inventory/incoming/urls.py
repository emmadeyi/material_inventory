from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='incomings'),
    path('add', views.add, name='add_incoming'),
    path('<int:incoming_id>/show', views.show, name='show_incoming'),
    path('<int:incoming_id>/edit', views.edit, name='edit_incoming'),
    path('search', views.search, name='search_incomings'),
]