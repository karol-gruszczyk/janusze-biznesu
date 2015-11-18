from .models import ShareGroup, Share
from django import forms


class ShareGroupForm(forms.ModelForm):
    class Meta:
        model = ShareGroup
        fields = ['verbose_name', 'shares']

    def __init__(self, *args, **kwargs):
        super(ShareGroupForm, self).__init__(*args, **kwargs)
        self.fields['shares'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['shares'].queryset = Share.objects.all()
