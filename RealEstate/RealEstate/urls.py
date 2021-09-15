

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.defaults import page_not_found

# from listing.views import  HomepageView
from django.views import generic


# handler404 = 'listing.views.handler404'
# handler500 = 'listing.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', page_not_found,
         {'exception': Exception('not found')}),
    path('accounts/', include('allauth.urls')),
    path('about/',generic.TemplateView.as_view(template_name='pages/about.html'),name='about'),
    path('faq/',generic.TemplateView.as_view(template_name='pages/faq.html'),name='faq'),
    path('contact/',generic.TemplateView.as_view(template_name='pages/contact.html'),name='contact'),
#     path('listing/', include('listing.urls')),
#     path('', HomepageView.as_view(), name='homepage'),
#     path('', include('authentication.urls')),
#     path('profile/', include('userprofile.urls')),
#     path('agency/', include('agency.urls')),
#     path('blogs/', include('blogs.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
