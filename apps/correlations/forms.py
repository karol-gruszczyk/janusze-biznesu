from django import forms

from .models import CorrelationSet
from apps.shares.models import ShareGroup


class CorrelationSetForm(forms.ModelForm):

    share_groups = forms.MultipleChoiceField(choices=((i, i.name) for i in ShareGroup.objects.all()), required=False)
    min_share_length = forms.IntegerField(min_value=0)

    class Meta:
        model = CorrelationSet
        fields = '__all__'

    def save(self, commit=True):
        # TODO
        return super(CorrelationSetForm, self).save(commit)
