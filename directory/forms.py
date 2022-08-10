from django.forms import ModelForm
from .models import Resource

class FormForResource(ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"