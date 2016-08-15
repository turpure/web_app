from django import forms


class AddForm(forms.Form):
    owner = forms.CharField()
    kw = forms.CharField()

