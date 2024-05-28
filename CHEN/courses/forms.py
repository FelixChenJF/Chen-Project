from django import forms
from .models import *

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
        
class OSCustomDataForm(forms.ModelForm):
    class Meta:
        model = OSCustomData
        fields = ['OSImage','OSText','OSLabel']
        labels = {
            'OSImage': 'Image',
            'OSText': 'Text',
            'OSLabel': 'Label'
        }
    