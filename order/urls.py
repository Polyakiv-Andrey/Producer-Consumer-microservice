from django.urls import path

from order.views import OrderListView, NewEmployee, DeleteOrderView

app_name = "order"
urlpatterns = [
    path('', OrderListView.as_view(), name="order-list"),
    path('new-employee/', NewEmployee.as_view(), name="new-employee"),
    path('delete/<int:pk>/', DeleteOrderView.as_view(), name="order-delete"),
]

