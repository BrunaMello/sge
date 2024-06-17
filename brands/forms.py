from django import forms

from . import models


class BrandForm(forms.ModelForm):
	class Meta:
		model = models.Brand
		fields = ['name', 'description']
		widgets = {
			'name': forms.TextInput({'class': 'form-control'}),
			'description': forms.Textarea({'class': 'form-control', 'rows': 3})
		}
		labels = {
			'name': 'Name',
			'description': 'Description'
		}
