from django import forms

class SaccoForm(forms.ModelForm):
    class Meta:
        model = "Saccos"

        