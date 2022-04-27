from django import forms


class PCNForm(forms.Form):
    pcn = forms.CharField(max_length=14, required=False)
    pcn_file = forms.FileField(required=False)
    