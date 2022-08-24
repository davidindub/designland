from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Resource, Profile


class FormForResource(LoginRequiredMixin, ModelForm):
    """
    Form for creating and updating design resources
    """
    class Meta:
        model = Resource
        fields = "__all__"
        exclude = ["approved", "slug", "upvotes", "bookmarks", "thumbnail"]


class FormForProfile(LoginRequiredMixin, ModelForm):
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