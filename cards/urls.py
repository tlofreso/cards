from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('households/', views.HouseholdListView.as_view(), name='household-list'),
    path('households/<int:pk>/', views.HouseholdDetailView.as_view(), name='household-detail'),
    path('households/create/', views.HouseholdCreateView.as_view(), name='household-create'),
    path('households/<int:pk>/update/', views.HouseholdUpdateView.as_view(), name='household-update'),
    path('households/<int:pk>/delete/', views.HouseholdDeleteView.as_view(), name='household-delete'),
    path('addresses/', views.AddressListView.as_view(), name='address-list'),
    path('addresses/<int:pk>/', views.AddressDetailView.as_view(), name='address-detail'),
    path('addresses/create/', views.AddressCreateView.as_view(), name='address-create'),
    path('addresses/<int:pk>/update/', views.AddressUpdateView.as_view(), name='address-update'),
    path('addresses/<int:pk>/delete/', views.AddressDeleteView.as_view(), name='address-delete'),
    path('individuals/', views.IndividualListView.as_view(), name='individual-list'),
    path('individuals/<int:pk>/', views.IndividualDetailView.as_view(), name='individual-detail'),
    path('individuals/create/', views.IndividualCreateView.as_view(), name='individual-create'),
    path('individuals/<int:pk>/update/', views.IndividualUpdateView.as_view(), name='individual-update'),
    path('individuals/<int:pk>/delete/', views.IndividualDeleteView.as_view(), name='individual-delete'),
]
