from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Resource, Profile
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class FormForResource(LoginRequiredMixin, forms.ModelForm):
    """
    Form for creating and updating design resources
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.disable_csrf = True

    class Meta:
        model = Resource
        exclude = ["approved", "author", "slug",
                   "upvotes", "bookmarks", "thumbnail"]

        labels = {
            "url": "URL",
            "content": "Description of the resource"
        }

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "url": forms.URLInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "tags": forms.TextInput(attrs={"class": "form-control"}),
        }


class FormForProfile(LoginRequiredMixin, forms.ModelForm):
    """
    Form for updating users profiles
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.disable_csrf = True

    class Meta:
        model = Profile
        prefix = 'profile'
        fields = ["username_github", "username_twitter", "website_address"]
        labels = {
            "username_github": "GitHub Username",
            "username_twitter": "Twitter Username",
            "website_address": "Portfolio or Personal Site URL"
        }
