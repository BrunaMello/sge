from django import forms
from django.core.exceptions import ValidationError

from . import models


class OutflowForm(forms.ModelForm):
	class Meta:
		model = models.Outflow
		fields = ['product', 'quantity', 'description']
		widgets = {
			'product': forms.Select({'class': 'form-control'}),
			'quantity': forms.NumberInput({'class': 'form-control'}),
			'description': forms.Textarea({'class': 'form-control', 'rows': 3})
		}
		labels = {
			'product': 'Product',
			'quantity': 'Quantity',
			'description': 'Description'
		}

	def clean_quantity(self):
		quantity = self.cleaned_data.get('quantity')  # Pegar a qtd de produtos que esta sendo retirada
		product = self.cleaned_data.get('product')  # Pegar a qtd de produtos que esta em estoque

		if quantity > product.quantity:
			raise ValidationError(
				f'Quantity for {product.title} is {product.quantity}. You can not withdraw more than {product.quantity}.'
			)
		return quantity
