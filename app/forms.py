from django import forms

from app.models import Data


class DataForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        max_length=50,
    )
    date = forms.CharField(
        label="Дата",
        max_length=16,
    ) # YYYY-MM-DD_HH:mm 
    class Meta:
        model = Data
        fields = ['name', 'date']