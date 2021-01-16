from django import forms

class SearchForm(forms.Form):
    search_text = forms.CharField()
    class Meta:
        fields = ['search_text']
    
    def __str__(self):
        return str(self.search_text)


class SelectForm(forms.Form):
    wikipedia = forms.BooleanField()
    stack= forms.BooleanField()
    wolfram = forms.BooleanField()
    google = forms.BooleanField()