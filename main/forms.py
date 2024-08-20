from .models import Events
from django.forms import ModelForm, TextInput, DateInput, Textarea

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'print_title', 'description', 'from_date', 'to_date']

        widgets = {
            "title" : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "print_title" : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название для печати'
            }),
            "from_date" : DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата начала'
            }),
            "to_date" : DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания'
            }),
            "description" : Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),



        }