
from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import Agent


class UserSignup(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserSignup, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'


class Login(LoginForm):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('company_name', 'country', 'about', 'state', 'city',
                  'zipcode', 'address', 'website', 'license', 'phone')


class AgentForm(SignupForm, AgentModelForm):

    def __init__(self, *args, **kwargs):
        super(AgentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'password1':
                visible.field.widget.attrs['placeholder'] = self.fields['password1'].label
            elif visible.name == 'password2':
                visible.field.widget.attrs['placeholder'] = self.fields['password2'].label
            elif visible.name == 'company_name':
                visible.field.widget.attrs['placeholder'] = ' '.join(visible.name.split('_')).title()
            else:
                visible.field.widget.attrs['placeholder'] = visible.name.title() 

        self.fields['website'].required = False

    def save(self, request):
        user = super(AgentForm, self).save(request)
        user.is_agent = True
        user.save()
        cleaned_data = self.agent_cleaned_data(self.cleaned_data)
        agent = Agent(user=user, **cleaned_data)
        agent.save()
        return user
    
    @staticmethod
    def agent_cleaned_data(data):
        removable_fields = ['password1', 'password2', 'email', 'username']
        for field in removable_fields:
            data.pop(field)
        return data
