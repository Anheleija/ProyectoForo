from django import forms
from .models import Post, Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Que pasa por tu mente?'}),
    max_length=4000, 
    help_text="Cantidad maxima de 4000 caracteres"
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]