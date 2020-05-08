from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='requisitions'),
    path('add', views.add, name='add_requisition'),
    path('<int:requisition_id>/show', views.show, name='show_requisition'),
    path('<int:requisition_id>/edit', views.edit, name='edit_requisition'),
    path('<int:requisition_id>/delete', views.delete, name='delete_requisition'),
]