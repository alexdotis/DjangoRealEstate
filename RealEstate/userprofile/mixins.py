from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import redirect_to_login


class AgentRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is agent."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not request.user.is_agent:
            return redirect(reverse('user_profile', kwargs={'pk': self.request.user.pk}))
    
        return super().dispatch(request, *args, **kwargs)


class UserRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and not agent."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if request.user.is_agent:
            return redirect(reverse('agent_profile', kwargs={'pk': self.request.user.pk}))
        return super().dispatch(request, *args, **kwargs)
