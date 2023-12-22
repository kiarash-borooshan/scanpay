from .models import Store
from django import forms


class AddPost(forms.ModelForm):
    class Meta:
        model = Store
        exclude = ("user", "created", "updated", "slug")