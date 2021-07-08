from django import forms
from .models import NoteData


# Form used to store data.
class NoteDataSave(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = NoteData
        exclude = ('user',)