from .models import Project
from django.forms import ModelForm
from django import forms

class ProProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('image',
                   'title',
                   'description',
                   'category',
                   'location',
                   'url',
        )
