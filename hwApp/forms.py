from django import forms
from nbformat.validator import validators

from hwApp import models


class AddBook(forms.Form):
    title = forms.CharField(label="title",max_length=100)
    # author = forms.ComboField(label="author",)
    author_id = forms.DecimalField(label="author id")
    price = forms.DecimalField(label="price",decimal_places=2, max_digits=10)
    published = forms.DateField(label="published in")