from django import forms
from .models import CommentData, Title, Label, CustomData

from django import forms
from .models import CustomData

class CustomForm(forms.ModelForm):
    class Meta:
        model = CustomData
        fields = ['text1', 'text2']
        labels = {
            'text1': 'Text in Chinese',
            'text2': 'Text in English',
        }


class CommentForm(forms.Form):
    class Meta:
        model = CommentData
        fields = ['message', 'label', 'label']
        labels = {
            'message': 'Message',
            'label': 'Label',
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
    