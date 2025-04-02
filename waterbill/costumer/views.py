from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Costumer, Employee, Bill
from django.db.models import Sum

# Dashboard View
def dashboard(request):
    context = {
        'total_costumers': Costumer.objects.count(),
        'total_employees': Employee.objects.count(),
        'total_bills': Bill.objects.count(),
        'total_outstanding_amount': Bill.objects.filter(status='U').aggregate(Sum('remaining_balance'))['remaining_balance__sum'] or 0,
        'recent_costumers': Costumer.objects.order_by('-id')[:5], 
    }
    return render(request, 'dashboard.html', context)

# Costumer Views
class CostumerListView(ListView):
    model = Costumer
    template_name = 'costumer/costumer_list.html'
    context_object_name = 'costumers'

class CostumerDetailView(DetailView):
    model = Costumer
    template_name = 'costumer/costumer_detail.html'

# Employee Views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'

# Bill Views
class BillListView(ListView):
    model = Bill
    template_name = 'bill/bill_list.html'
    context_object_name = 'bills'

class BillDetailView(DetailView):
    model = Bill
    template_name = 'bill/bill_detail.html'
