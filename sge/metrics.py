from django.db.models import Sum, F
from django.utils import timezone
from django.utils.formats import number_format

from outflows.models import Outflow
from products.models import Product


def get_product_metrics():
	# Return all the products from the database
	products = Product.objects.all()

	# Interation for sum all the values of the products
	total_cost_price = sum(product.cost_price * product.quantity for product in products)
	total_selling_price = sum(product.selling_price * product.quantity for product in products)
	total_quantity = sum(product.quantity for product in products)  # Sum all the quantities of the products
	total_profit = total_selling_price - total_cost_price  # Calculate the total profit

	return dict(
		total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
		total_selling_price=number_format(total_selling_price, decimal_pos=2, force_grouping=True),
		total_quantity=total_quantity,
		total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
	)


def get_sales_metrics():
	total_sales = Outflow.objects.count()
	total_products_sold = Outflow.objects.aggregate(total_products_sold=Sum('quantity'))['total_products_sold'] or 0
	total_sales_value = sum(outflow.quantity * outflow.product.selling_price for outflow in Outflow.objects.all())
	total_sales_cost = sum(outflow.quantity * outflow.product.cost_price for outflow in Outflow.objects.all())
	total_sales_profit = total_sales_value - total_sales_cost

	return dict(
		total_sales=number_format(total_sales, force_grouping=True),
		total_products_sold=total_products_sold,
		total_sales_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
		total_sales_profit=number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
	)


def get_daily_sales_data():
	today = timezone.now().date()
	dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
	values = list()

	for date in dates:
		sales_total = Outflow.objects.filter(
			created_at__date=date
		).aggregate(
			total_sales=Sum(F('product__selling_price') * F('quantity'))
		)['total_sales'] or 0
		values.append(float(sales_total))

	return dict(
		dates=dates,
		values=values,
	)


def get_daily_sales_quantity_data():
	today = timezone.now().date()
	dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
	quantities = list()

	for date in dates:
		sales_quantity = Outflow.objects.filter(created_at__date=date).count()
		quantities.append(sales_quantity)

	return dict(
		dates=dates,
		values=quantities,
	)
