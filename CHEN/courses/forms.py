from django import forms
from .models import CommentData, Title, Label, CustomData

class CustomForm(forms.Form):
    class Meta:
        model = CustomData
        fields = ['text1', 'text2', 'label']
        labels = {
            'text1': 'Text1',
            'text2': 'Text2',
            'label': 'Label',
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
    