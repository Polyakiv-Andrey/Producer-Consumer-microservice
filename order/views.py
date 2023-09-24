import datetime

from django.contrib import messages
from django.contrib.auth import get_user_model

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from Producer_Consumer_microservice.settings import BOT_TOKEN
from order.models import Order
from order.tasks import send_telegram_message

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
        chat_id = self.request.COOKIES.get('chat_id')
        if chat_id and BOT_TOKEN:
            send_telegram_message.delay(chat_id, message)
        return redirect('order:order-list')
