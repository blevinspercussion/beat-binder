from django import forms
from .models import Score 
from taggit.forms import TagWidget 

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score 
        fields = [
            'title',
            'composer',
            'arranger',
            'instruments',
            'time_signature',
            'difficulty',
            'description',
            'tags',
            'pdf_file',
            'public',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'instruments': TagWidget(attrs={'placeholder': 'e.g. snare drum, marimba, etc.'}),
            'tags': TagWidget(attrs={'placeholder': 'exercise, warmup, transcription, odd time, etc.'}),
            'pdf_file': forms.FileInput(attrs={'class': 'form-control-file'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_pdf_file(self):
        pdf = self.cleaned_data.get('pdf_file')
        if pdf and not pdf.name.endswith('.pdf'):
            raise forms.ValidationError("File must be a PDF")
        return pdf