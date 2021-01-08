from django import forms
from .models import obra

class Obraform(forms.ModelForm):
    class Meta:
        model = obra
        fields=[
            'cod_work_sq',
            'ISWC',
            'titulo',
            'autor',
            'persona',
        ]