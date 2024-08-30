from .models import Tweet
from django import forms

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        labels = {
            'tweet': 'Tweet',
            'photo': 'Photo'
        }
        widgets = {
            'tweet': forms.Textarea(attrs={'rows': 5, 'cols': 20}),
        }
