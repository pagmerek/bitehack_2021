from django import forms

class SearchForm(forms.Form):
    search_text = forms.CharField()
    class Meta:
        fields = ['search_text']
    
    def __str__(self):
        return str(self.search_text)