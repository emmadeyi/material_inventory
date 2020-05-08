from django import forms
from .models import Requisition

#DataFlair
class RequisitionCreate(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}), 
            'due_date': forms.TextInput(attrs={'class': 'validate datepicker add_due_date', 'placeholder': 'Select Due Date'}),
        }