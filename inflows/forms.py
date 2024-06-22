from django import forms

from . import models


class InflowForm(forms.ModelForm):
	class Meta:
		model = models.Inflow
		fields = ['supplier', 'product', 'quantity', 'description']
		widgets = {
			'supplier': forms.Select({'class': 'form-control'}),
			'product': forms.Select({'class': 'form-control'}),
			'quantity': forms.NumberInput({'class': 'form-control'}),
			'description': forms.Textarea({'class': 'form-control', 'rows': 3})
		}
		labels = {
			'product': 'Product',
			'supplier': 'Supplier',
			'quantity': 'Quantity',
			'description': 'Description'
		}
