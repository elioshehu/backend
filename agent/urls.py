from django.urls import path

from agent.customer_api_views.customer_views import CustomerListCreateAPIView

urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name='customers'),
    path('users/', UserListCreateAPIView.as_view(), name='users'),
]
