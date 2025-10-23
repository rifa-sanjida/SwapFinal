from django import forms
from .models import Item, Message

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'item_type', 'name', 'description', 'price', 'condition', 'location', 'contact_info', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'contact_info': forms.Textarea(attrs={'rows': 3}),
        }


