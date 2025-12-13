from django import forms
from .models import JobCard


class JobCardForm(forms.ModelForm):
    class Meta:
        model = JobCard
        fields = [
            'full_name',
            'department',
            'phone_number',
            'email_address',
            'vehicle_make_model',
            'year',
            'registration_number',
            'mileage',
            'vin_chassis_number',
            'service_description',
            'serviced_recently',
            'preferred_service_date',
            'additional_concerns',
            'confirmation'
        ]

        widgets = {
            'preferred_service_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'service_description': forms.Textarea(attrs={'rows': 3}),
            'additional_concerns': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_confirmation(self):
        confirmation = self.cleaned_data.get('confirmation')
        if not confirmation:
            raise forms.ValidationError(
                "You must confirm that the details provided are accurate."
            )
        return confirmation
