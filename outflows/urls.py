from django.urls import path

from . import views

urlpatterns = [
	path('outflow/list/', views.OutflowListView.as_view(), name='outflow_list'),
	path('outflow/create/', views.OutflowCreateView.as_view(), name='outflow_create'),
	path('outflow/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow_detail'),
]
