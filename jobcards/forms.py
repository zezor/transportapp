from django import forms
from .models import JobCard

from django import forms
from .models import JobCard

class JobCardForm(forms.ModelForm):
    class Meta:
        model = JobCard
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })


    def clean_confirmation(self):
        confirmation = self.cleaned_data.get('confirmation')
        if not confirmation:
            raise forms.ValidationError(
                "You must confirm that the details provided are accurate."
            )
        return confirmation
