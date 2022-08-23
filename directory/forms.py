from django.forms import ModelForm
from .models import Resource, Profile

class FormForResource(ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"

class FormForProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ["username_github", "username_twitter"]
        labels = {
            "username_github": "GitHub",
            "username_twitter": "Twitter"
        }