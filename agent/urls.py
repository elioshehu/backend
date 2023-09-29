from django.urls import path

from agent.customer_api_views.customer_views import CustomerListCreateAPIView, UserListCreateAPIView, \
    GroupListCreateAPIView, CustomerListUpdateDestroyAPIView, UserListUpdateDestroyAPIView, \
    GroupListUpdateDestroyAPIView

urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name='customers'),
    path('customersUpdate/<int:id>', CustomerListUpdateDestroyAPIView.as_view(), name='customersUD'),
    path('users/', UserListCreateAPIView.as_view(), name='users'),
    path('usersUpdate/<int:id>', UserListUpdateDestroyAPIView.as_view(), name='usersUD'),
    path('groups/', GroupListCreateAPIView.as_view(), name='groups'),
    path('groupsUpdate/<int:id>', GroupListUpdateDestroyAPIView.as_view(), name='groupsUD'),
    # path('usergroups/', UserGroupsListCreateAPIView.as_view(), name='usergroups'),
]
