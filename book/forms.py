from django import forms
from .models import Book, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        labels = {
            'category': 'Category'
        }
        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category', 'blank':'True'})
        }


class BookForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects, empty_label=None, blank=True, widget=forms.Select)

    class Meta:
        model = Book
        fields = ['id', 'title', 'subtitle', 'authors', 'publisher', 'published_date', 'category', 'distribution_expense']
        labels = {
            'id': 'Id',
            'title': 'Title',
            'subtitle': 'Subtitle',
            'authors': 'Authors',
            'publisher': 'Publisher',
            'published_date': 'Published Date',
            'category': 'Category',
            'distribution_expense': 'Expense',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Id'}),
            'title': forms.Textarea(attrs={'class':'form-control', 'rows':'5', 'placeholder':'Title'}),
            'subtitle': forms.Textarea(attrs={'class':'form-control', 'rows':'5', 'placeholder':'Subtitle'}),
            'authors': forms.Textarea(attrs={'class':'form-control', 'rows':'5', 'placeholder':'Authors'}),
            'publisher': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Publisher'}),
            'published_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Published Date  yyyy-mm-dd'}),
            #'category': 
            'distribution_expense': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Expense'}),
        }



