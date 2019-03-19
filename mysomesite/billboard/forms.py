from django.forms import ModelForm

from .models import Advertisement, Rubric


class AdvForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'content', 'price', 'rubric')
