from django.urls import path

from agent.customer_api_views.customer_views import CustomerListCreateAPIView, UserListCreateAPIView, \
    CustomerListUpdateDestroyAPIView, UserListUpdateDestroyAPIView,ShitesListCreateAPIView, ShitesUpdateAPIView

urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name='customers'),
    path('customers/<int:pk>', CustomerListUpdateDestroyAPIView.as_view(), name='customersUD'),
    path('users/', UserListCreateAPIView.as_view(), name='users'),
    path('usersUpdate/<int:id>', UserListUpdateDestroyAPIView.as_view(), name='usersUD'),
    path('users/Shites', ShitesListCreateAPIView.as_view(), name='shites'),
    path('users/ShitesUpdate/<int:id>', ShitesUpdateAPIView.as_view(), name='shitesUpdate'),
    # path('groups/', GroupListCreateAPIView.as_view(), name='groups'),
    # path('groupsUpdate/<int:id>', GroupListUpdateDestroyAPIView.as_view(), name='groupsUD'),

    # rregullo shites - vendos vetem nje grup shites per krijimin e user
]
