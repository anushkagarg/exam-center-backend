from django import forms
from django.contrib.postgres.forms.array import SimpleArrayField

from .models import Submission


class SubmissionForm(forms.ModelForm):
    answers = SimpleArrayField(SimpleArrayField(forms.CharField()), delimiter='|')
    class Meta:
        model = Submission
        fields = '__all__'

    