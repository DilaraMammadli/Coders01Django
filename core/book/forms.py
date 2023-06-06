from django import forms
from .models import Book
 
# class BookForm(forms.Form):
#     name =  forms.CharField()
#     author_name = forms.CharField()
#     content = forms.CharField()

class BookForm(forms.ModelForm):

    # category = forms.CharField()
    class Meta:
        model = Book
        fields = ("name", "author_name", "content")