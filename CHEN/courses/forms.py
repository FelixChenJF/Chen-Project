from django import forms

from .models import Title, Label

class CustomForm(forms.Form):
    class Meta:
        model = Title
        fields = ['text1', 'text2', 'label', 'title']
        labels = {
            'text1': 'Text1',
            'text2': 'Text2',
            'label': 'Label',
            'title': 'Title',
        }

class CommentForm(forms.Form):
    class Meta:
        model = Title
        fields = ['message', 'label', 'label', 'title']
        labels = {
            'message': 'Message',
            'label': 'Label',
            'title': 'Title',
        }

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title']
        labels = {
            'title': 'Title',
        }
        
class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['label', 'title']
        labels = {
            'label': 'Label',
            'title': 'Title'
        }
    