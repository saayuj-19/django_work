from django.urls import path
from . import views
from .views import CostumerListView, EmployeeListView, BillListView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('costumers/', CostumerListView.as_view(), name='costumer-list'),

    path('employees/', EmployeeListView.as_view(), name='employee-list'),

    path('bills/', BillListView.as_view(), name='bill-list'),
]
