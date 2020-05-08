from django.contrib import admin

# Register your models here.
from .models import Requisition

class RequisitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'quantity', 'unit', 'status', 'due_date')
    list_display_links = ('id', 'item')
    list_filter = ('status', 'originator', 'authorizer', 'approver')
    list_editable = ('status',)
    search_fields = ('item', 'description', 'quantity', 'unit', 'status', 'due_date')
    list_per_page = 3

admin.site.register(Requisition, RequisitionAdmin)
