from django.http.response import HttpResponseRedirect
from .models import AssignmentProperty
from django.views import generic
from authentication.models import User, Agent
from .forms import (
    AgentProfileUpdateForm,
    UserUpdateForm,
    UserAddListingForm,
    FeatureForm,
    ImagesForm,
    AgentPropertyCreateForm,
    UserListingUpdateForm
)

from django.urls import reverse
from django.contrib import messages

from listing.models import Listing
from .mixins import AgentRequiredMixin, UserRequiredMixin
from rest_framework.views import APIView
from listing.choices import display_subcategory_dictionary

from rest_framework.response import Response

# Agents


class AgentProfileUpdateView(AgentRequiredMixin, generic.UpdateView):
    """Agent Profile and Update"""
    template_name = 'UserProfile/core/update_profile.html'
    form_class = AgentProfileUpdateForm

    def get_object(self, queryset=None):
        return Agent.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):

        context = super(AgentProfileUpdateView,
                        self).get_context_data(**kwargs)
        instance = User.objects.get(username=self.request.user.username)
        if self.request.POST:
            """Base form contains username, first_name, last_name"""
            context['base_form'] = UserUpdateForm(
                self.request.POST, instance=instance)
        else:
            context['base_form'] = UserUpdateForm(instance=instance)

        return context

    def form_valid(self, form):
        ctx = self.get_context_data()
        base_form = ctx['base_form']
        if base_form.is_valid():
            base_form.save()
        return super(AgentProfileUpdateView, self).form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, 'agent updated')
        return reverse('agent_profile', kwargs={'pk': self.request.user.pk})


class AgentPropertyCreateView(AgentRequiredMixin, generic.CreateView):
    """Agent Create property with forms"""
    model = Listing
    form_class = AgentPropertyCreateForm
    template_name = 'UserProfile/core/create_property.html'

    def get_success_url(self):
        messages.success(self.request, 'property added')
        return reverse('agent_create_property')

    def get_context_data(self, **kwargs):
        context = super(AgentPropertyCreateView,
                        self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = AgentPropertyCreateForm(self.request.POST)
            context['feature_form'] = FeatureForm(self.request.POST)
            context['images_form'] = ImagesForm(
                self.request.POST, self.request.FILES)
        else:

            context['feature_form'] = FeatureForm()
            context['images_form'] = ImagesForm()
        return context

    def form_valid(self, form):
        ctx = self.get_context_data()
        features = ctx['feature_form']
        images_form = ctx['images_form']
        if form.is_valid() and features.is_valid() and images_form.is_valid():
            agent = Agent.objects.get(user=self.request.user)
            instance = form.save(commit=False)
            instance.agent = agent
            instance.save()

            self.object = instance
            features.instance = self.object
            features.save()
            images_form.instance = self.object
            images_form.save()
        return super(AgentPropertyCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

# For agents only


class UserAssignedPropertyListView(AgentRequiredMixin, generic.ListView):
    """Properties that user assigned"""
    model = AssignmentProperty
    template_name = 'UserProfile/agent/user_assigned_property_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = AssignmentProperty.objects.filter(
            agency__user__username=self.request.user, is_assigned=False)
        print(qs.count())
        return qs

    def post(self, request, *args, **kwargs):
        """Remove AssignmentProperty by user"""
        if request.POST:
            object_id = request.POST.get('object_id')
            agent = Agent.objects.get(user=request.user)
            AssignmentProperty.objects.get(id=object_id).agency.remove(agent)
            return HttpResponseRedirect(reverse('user_assigned_properties'))

        return super(UserAssignedPropertyListView, self).get(request, *args, **kwargs)


# For agents only
class UserAssignedPropertyDetailView(AgentRequiredMixin, generic.DetailView):
    """Properties detail view that user assigned. Details about user and property"""
    model = AssignmentProperty
    template_name = 'UserProfile/agent/user_assigned_property_detail.html'

    def get_queryset(self):
        qs = AssignmentProperty.objects.filter(
            agency__user__username=self.request.user, is_assigned=False)
        return qs


class AgentPropertyListView(AgentRequiredMixin, generic.ListView):
    """Properties that agent has"""
    model = Agent
    template_name = 'UserProfile/agent/property_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = Listing.objects.filter(
            agent__user__username=self.request.user)
        return qs


class AgentPropertyUpdateView(AgentRequiredMixin, generic.UpdateView):
    """Agent can update the property"""
    model = Listing
    form_class = AgentPropertyCreateForm
    template_name = 'UserProfile/core/update_property.html'

    def get_queryset(self):
        return Listing.objects.filter(agent__user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, 'property updated')
        return reverse('agent_property_list')

    def get_context_data(self, **kwargs):
        context = super(AgentPropertyUpdateView,
                        self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = AgentPropertyCreateForm(
                self.request.POST, instance=self.object)
            context['feature_form'] = FeatureForm(
                self.request.POST, instance=self.object)
            context['images_form'] = ImagesForm(
                self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['form'] = AgentPropertyCreateForm(instance=self.object)
            context['feature_form'] = FeatureForm(instance=self.object)
            context['images_form'] = ImagesForm(instance=self.object)
        return context

    def form_valid(self, form):
        ctx = self.get_context_data()
        feature_form = ctx['feature_form']
        images_form = ctx['images_form']
        if form.is_valid() and feature_form.is_valid() and images_form.is_valid():
            form.save()
            feature_form.save()
            images_form.save()
        return super(AgentPropertyUpdateView, self).form_valid(form)


class AgentDeleteProperty(AgentRequiredMixin, generic.DeleteView):
    model = Listing

    def get_success_url(self) -> str:
        return reverse('agent_profile', kwargs={'pk': self.request.user.pk})

# Users


class UserProfileUpdateView(UserRequiredMixin, generic.UpdateView):
    """User profile and update"""
    template_name = 'UserProfile/core/update_profile.html'
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.pk)

    def get_success_url(self) -> str:
        messages.success(self.request, 'user updated')
        return reverse('user_profile', kwargs={'pk': self.request.user.pk})


class UserPropertyCreateView(UserRequiredMixin, generic.CreateView):
    """User can assing a property"""
    model = AssignmentProperty
    form_class = UserAddListingForm
    template_name = 'UserProfile/core/create_property.html'

    def get_success_url(self) -> str:
        messages.success(self.request, 'property Added')
        return reverse('user_create_property')

    def form_valid(self, form):
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()

        return super(UserPropertyCreateView, self).form_valid(form)


class UserPropertyListView(UserRequiredMixin, generic.ListView):
    """Users assigned properties"""
    model = AssignmentProperty
    template_name = 'UserProfile/user/property_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = AssignmentProperty.objects.filter(user=self.request.user)
        return qs


class UserPropertyUpdateView(UserRequiredMixin, generic.UpdateView):
    """User can update property that assigned"""
    model = AssignmentProperty
    form_class = UserListingUpdateForm
    template_name = 'UserProfile/core/update_property.html'

    def get_success_url(self) -> str:
        messages.success(self.request, 'property Updated')
        return reverse('user_properties')

    def get_queryset(self):
        qs = AssignmentProperty.objects.filter(
            user=self.request.user, is_assigned=False)
        return qs


class SubCategoryApiView(APIView):

    def get(self, request):
        json_data = display_subcategory_dictionary()
        return Response({'fields': json_data})
