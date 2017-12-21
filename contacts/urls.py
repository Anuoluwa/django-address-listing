from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.ContactListView.as_view(), name='contacts'),
    url(r'^list/(?P<pk>\d+)$', views.ContactDetailView.as_view(), name='contact-detail'),
]

urlpatterns += [
    url(r'^create/$', views.ContactCreate.as_view(), name='contact_create'),
    url(r'^(?P<pk>\d+)/update/$', views.ContactUpdate.as_view(), name='contact_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ContactDelete.as_view(), name='contact_delete'),
]
