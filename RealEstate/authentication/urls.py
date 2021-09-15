from django.urls import path
from .views import AgentFormView, UserFormView

urlpatterns = [
    path('accounts/signup/agent/', AgentFormView.as_view(), name='agent-form'),
    path('accounts/signup/user/', UserFormView.as_view(), name='account_signup'),

]
