from django import forms


class HomeForm(forms.Form):
    post = forms.CharField()

class QueryForm(forms.Form):
     post = forms.CharField()
