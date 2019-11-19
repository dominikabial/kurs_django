from django import forms
from .models import Comment

#class CommentForm(forms.Form):
#    name = forms.CharField()
#    email = forms.EmailField()
#    text = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['book']
