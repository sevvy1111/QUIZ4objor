from django import forms

from jobs.models import Job


class JobForm(forms.ModelForm):
    job_title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter job title',
        }
    ))

    job_description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter job description',
            'rows': 5,
        }
    ))

    location = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter job location',
        }
    ))

    min_offer = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter minimum offer',
        }
    ))

    max_offer = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter maximum offer',
        }
    ))

    class Meta:
        model = Job
        fields = ['job_title', 'job_description', 'location', 'min_offer', 'max_offer']

    def clean_job_title(self):
        job_title = self.cleaned_data.get('job_title')
        if not job_title:
            raise forms.ValidationError("Job title cannot be empty.")
        return job_title

    def clean_job_description(self):
        job_description = self.cleaned_data.get('job_description')
        if not job_description:
            raise forms.ValidationError("Job description cannot be empty.")
        return job_description

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if not location:
            raise forms.ValidationError("Job location cannot be empty.")
        return location

    def clean_min_offer(self):
        min_offer = self.cleaned_data.get('min_offer')
        if min_offer is None or min_offer < 0:
            raise forms.ValidationError("Minimum offer must be a positive number.")
        return min_offer

    def clean_max_offer(self):
        max_offer = self.cleaned_data.get('max_offer')
        if max_offer is None or max_offer < 0:
            raise forms.ValidationError("Maximum offer must be a positive number.")
        return max_offer

    def clean(self):
        cleaned_data = super().clean()
        min_offer = cleaned_data.get('min_offer')
        max_offer = cleaned_data.get('max_offer')

        if min_offer is not None and max_offer is not None and min_offer > max_offer:
            raise forms.ValidationError("Minimum offer cannot be greater than maximum offer.")

        return cleaned_data