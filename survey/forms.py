from django import forms
from django.forms import modelformset_factory, formset_factory

from .models import Survey, Field, MultipleChoice


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title', 'subtitle', 'tag',)


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('question',)   # 'type',


ChoiceFormSet = modelformset_factory(
    MultipleChoice,
    fields=['choice_text'],
    extra=1,
    widgets={
        'choice_text': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter choice text',
            }
        )
    }
)


class TextAnswerForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['question']
