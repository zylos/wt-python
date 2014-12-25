from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^dataset/$', 
        views.DataSetList.as_view(), 
        name='dataset-list'),
    url(r'^dataset/(?P<pk>[0-9a-z]+)/$', 
        views.DataSetDetail.as_view(),
        name='dataset-detail'),
    url(r'^dataset/(?P<pk>[0-9a-z]+)/resource/$', 
        views.DataSetResourceList.as_view(),
        name='dataset-resource-list'),
    url(r'^dataset/(?P<pk>[0-9a-z]+)/resource/(?P<pk_res>[0-9a-z]+)$', 
        views.DataSetResourceDetail.as_view(),
        name='dataset-resource-detail'),
    url(r'^dataset/(?P<pk>[0-9a-z]+)/extra/$', 
        views.DataSetExtraList.as_view(),
        name='dataset-extra-list'),
    url(r'^dataset/(?P<pk>[0-9a-z]+)/extra/(?P<pk_extra>[0-9a-zA-Z_\-\s]+)$', 
        views.DataSetExtraDetail.as_view(),
        name='dataset-extra-detail'),
    url(r'^dataset/(?P<pk>[0-9a-z]+)/rate/(?P<rating>[0-9])$', 
        views.DataSetRate.as_view(),
        name='dataset-rate'),

    url(r'^resource/$', 
        views.ResourceList.as_view(), 
        name='resource-list'),
    url(r'^resource/(?P<pk>[0-9a-z]+)/$', 
        views.ResourceDetail.as_view(),
        name='resource-detail'),

    url(r'^group/$', 
        views.GroupList.as_view(), 
        name='group-list'),
    url(r'^group/(?P<pk>[0-9a-z]+)/$', 
        views.GroupDetail.as_view(),
        name='group-detail'),

    url(r'^tag/$', 
        views.TagList.as_view(),
        name='tag-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),

    url(r'^logged_in/$', views.logged_in, name='logged_in'),
    url(r'^login_error/$', views.login_error, name='login_error'),
    url(r'^logout/$', views.logout, name='logout'),
]