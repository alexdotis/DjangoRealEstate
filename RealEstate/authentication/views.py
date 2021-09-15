from .forms import AgentForm, UserSignup
from allauth.account.views import SignupView


class AgentFormView(SignupView):
    form_class = AgentForm
    template_name = 'account/agent_signup.html'


class UserFormView(SignupView):
    form_class = UserSignup
    template_name = 'account/signup.html'
