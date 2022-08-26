from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Resource, Profile
from taggit.models import Tag
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

TAGS = []

for tag in Tag.objects.all():
    TAGS.append((tag, tag))


class FormForResource(LoginRequiredMixin, forms.ModelForm):
    """
    Form for creating and updating design resources
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.form_action = ""
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta:
        model = Resource
        # fields = "__all__"
        exclude = ["approved", "slug", "upvotes", "bookmarks", "thumbnail"]

        labels = {
            "url": "URL",
            "content": "Description of the resource"
        }


        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "url": forms.URLInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "tags": forms.CheckboxSelectMultiple(choices=TAGS),
            
        }


class FormForProfile(LoginRequiredMixin, forms.ModelForm):
    """
    Form for updating users profiles
    """
    class Meta:
        model = Profile
        fields = ["username_github", "username_twitter", "website_address"]
        labels = {
            "username_github": "GitHub",
            "username_twitter": "Twitter",
            "website_address": "Portfolio URL"
        }