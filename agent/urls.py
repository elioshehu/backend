from django.urls import path

from agent.customer_api_views.customer_views import CustomerListCreateAPIView, UserListCreateAPIView, \
    GroupListCreateAPIView

urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name='customers'),
    path('users/', UserListCreateAPIView.as_view(), name='users'),
    path('groups/', GroupListCreateAPIView.as_view(), name='groups'),
    # path('usergroups/', UserGroupsListCreateAPIView.as_view(), name='usergroups'),
]
