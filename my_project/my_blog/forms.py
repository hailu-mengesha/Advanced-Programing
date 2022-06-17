from django import forms
from .models import Post

from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model=Post
        fields=('title','content')



class PostUpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content')
        '''def __init__(self,*args,**kwargs):
            super(PostUpdateForm,self).__init__(*args,**kwargs)

            for fieldname in ['username','email']:
                self.fields[fieldname].help_text=None'''