from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':''}),required=False)
    content = forms.CharField(widget=PagedownWidget(show_preview=False,attrs={'class':'form-control'}),label='Body')
    publish = forms.DateField(widget=forms.SelectDateWidget)
    draft = forms.BooleanField(widget=forms.Select(choices=((1,'Yes'),(0,'No'))))
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]