from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Household, Address, Individual

class HomePageView(TemplateView):
    template_name = 'cards/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['household_count'] = Household.objects.filter(created_by=self.request.user).count()
            context['address_count'] = Address.objects.filter(household__created_by=self.request.user).count()
            context['individual_count'] = Individual.objects.filter(household__created_by=self.request.user).count()
        return context

class HouseholdListView(ListView):
    model = Household
    template_name = 'cards/household_list.html'
    context_object_name = 'households'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Household.objects.filter(created_by=self.request.user)
        else:
            # For unauthenticated users, return an empty queryset
            return Household.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            context['message'] = "Please log in to view your households."
        return context

class HouseholdDetailView(DetailView):
    model = Household
    template_name = 'cards/household_detail.html'

class HouseholdCreateView(CreateView):
    model = Household
    template_name = 'cards/household_form.html'
    fields = ['name', 'address']
    success_url = reverse_lazy('household-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class HouseholdUpdateView(UpdateView):
    model = Household
    template_name = 'cards/household_form.html'
    fields = ['name', 'address']
    success_url = reverse_lazy('household-list')

class HouseholdDeleteView(DeleteView):
    model = Household
    template_name = 'cards/household_confirm_delete.html'
    success_url = reverse_lazy('household-list')

class AddressListView(ListView):
    model = Address
    template_name = 'cards/address_list.html'
    context_object_name = 'addresses'

class AddressDetailView(DetailView):
    model = Address
    template_name = 'cards/address_detail.html'

class AddressCreateView(CreateView):
    model = Address
    fields = ['street', 'city', 'state', 'zipcode', 'country']
    template_name = 'cards/address_form.html'
    success_url = reverse_lazy('address-list')

class AddressUpdateView(UpdateView):
    model = Address
    fields = ['street', 'city', 'state', 'zipcode', 'country']
    template_name = 'cards/address_form.html'
    success_url = reverse_lazy('address-list')

class AddressDeleteView(DeleteView):
    model = Address
    template_name = 'cards/address_confirm_delete.html'
    success_url = reverse_lazy('address-list')

class IndividualListView(ListView):
    model = Individual
    template_name = 'cards/individual_list.html'
    context_object_name = 'individuals'

class IndividualDetailView(DetailView):
    model = Individual
    template_name = 'cards/individual_detail.html'

class IndividualCreateView(CreateView):
    model = Individual
    template_name = 'cards/individual_form.html'
    fields = ['first_name', 'last_name', 'household']
    success_url = reverse_lazy('individual-list')

class IndividualUpdateView(UpdateView):
    model = Individual
    template_name = 'cards/individual_form.html'
    fields = ['first_name', 'last_name', 'household']
    success_url = reverse_lazy('individual-list')

class IndividualDeleteView(DeleteView):
    model = Individual
    template_name = 'cards/individual_confirm_delete.html'
    success_url = reverse_lazy('individual-list')