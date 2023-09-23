import datetime

from django.contrib import messages
from django.contrib.auth import get_user_model

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from order.models import Order

Employee = get_user_model()


class NewEmployee(View):

    def get(self, request, *args, **kwargs):
        Employee.create_employee()
        return redirect('order:order-list')


class OrderListView(generic.ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all().order_by('-task_id')


class DeleteOrderView(generic.DeleteView):
    model = Order
    success_url = reverse_lazy('order-list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        message = (
            f"Task №-{self.object.task_id} with the title {self.object.name} " 
            f"was processed by {self.object.employee} at {datetime.datetime.now()}"
        )
        self.object.delete()
        messages.success(self.request, message)
        return redirect('order:order-list')
