from django import forms

from . import models


class ProductForm(forms.ModelForm):
	class Meta:
		model = models.Product
		fields = ['title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'category': forms.Select(attrs={'class': 'form-control'}),
			'brand': forms.Select(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
			'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
			'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
		}
		labels = {
			'title': 'Title',
			'category': 'Category',
			'brand': 'Brand',
			'description': 'Description',
			'serie_number': 'Serie Number',
			'cost_price': 'Cost Price',
			'selling_price': 'Selling Price',
		}
