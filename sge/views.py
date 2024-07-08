from django.shortcuts import render


def home(request):
	product_metrics = {
		'total_cost_price': 100000,
		'total_selling_price': 200000,
		'total_quantity': 1000,
		'total_profit': 100000,
	}

	context = {
		'product_metrics': product_metrics,
	}

	return render(request, 'home.html', context)
