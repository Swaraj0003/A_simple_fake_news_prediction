from django import forms

class NewsForm(forms.Form):
    news_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}), label='Enter News Text')
