from .models import Store, Comment
from django import forms
from ckeditor.widgets import CKEditorWidget


class AddPost(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Store
        exclude = ("user", "created", "updated", "slug")


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(widget=forms.EmailInput,
                            max_length=100)
    message = forms.CharField(widget=forms.Textarea)
