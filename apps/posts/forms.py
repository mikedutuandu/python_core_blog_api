from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    title = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
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

    # VALIDATION-----------------------------------------------------------
    # def clean(self):
    #     cleaned_data = super(PostForm, self).clean()
    #     data = cleaned_data.get('title')
    #     if "fred@example.com" != data:
    #         # raise forms.ValidationError("You have forgotten about Fred!")
    #         self.add_error('title', '2 you')

    #
    # def clean_title(self):
    #     data = self.cleaned_data['title']
    #     if "fred@example.com" != data:
    #         raise forms.ValidationError("You have forgotten about Fred!")
    #     return data
