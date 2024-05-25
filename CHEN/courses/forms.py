from django import forms

class CustomForm(forms.Form):
    audio1 = forms.FileField(label='Chinese Audio', required=False)
    text1 = forms.CharField(label='Chinese Text', widget=forms.Textarea, required=False)
    audio2 = forms.FileField(label='English Audio', required=False)
    text2 = forms.CharField(label='English Text', widget=forms.Textarea, required=False)
    message = forms.CharField(label='Comments', widget=forms.Textarea, required=False)

class TitleForm(forms.Form):
    title = forms.CharField(max_length=200)