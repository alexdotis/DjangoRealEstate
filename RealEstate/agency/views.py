from listing.models import Listing
from authentication.models import Agent
from django.views import generic
from django.core.paginator import Paginator
# Agency


class AgenyListView(generic.ListView):
    template_name = 'Agency/agency_list.html'
    model = Agent
    paginate_by = 10


class AgencyDetailView(generic.DetailView):
    template_name = 'Agency/agency_profile.html'
    model = Agent

    def get_object(self, queryset=None):
        qs = Agent.objects.get(company_name=self.kwargs['user'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(AgencyDetailView, self).get_context_data(**kwargs)
        query = Listing.objects.filter(agent__company_name=self.kwargs['user'])
    
        page = self.request.GET.get('page')
        context['agency'] = Paginator(query, 10).get_page(page)

        return context
