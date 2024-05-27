from django import forms
from .models import OSLabel, OSTitle, Title, Label, CustomData

class CustomForm(forms.ModelForm):
    class Meta:
        model = CustomData
        fields = ['text1', 'text2', 'message', 'label']
        labels = {
            'text1': 'Text in Chinese',
            'text2': 'Text in English',
            'message': 'Message',
            'label': 'Label: '
        }

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title']
        labels = {
            'title': 'Title',
        }
        
class OSTitleForm(forms.ModelForm):
    class Meta:
        model = OSTitle
        fields = ['OSTitle']
        labels = {
            'OSTitle': 'Title',
        }
        
class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['label', 'title']
        labels = {
            'label': 'Label',
            'title': 'Title'
        }
        
class OSLabelForm(forms.ModelForm):
    class Meta:
        model = OSLabel
        fields = ['OSLabel', 'OSTitle']
        labels = {
            'OSLabel': 'Label',
            'OSTitle': 'Title'
        }
    