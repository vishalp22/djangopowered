from django.conf.urls import url, include
from newsletter.views import home, contact
from Django18.views import about


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
]
