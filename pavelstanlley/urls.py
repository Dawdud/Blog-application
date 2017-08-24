from django.conf.urls import url

import views as myapp_views


urlpatterns = [

                     url(r'^$', myapp_views.index, name='index'),
                     url(r'about/', myapp_views.about, name='about'),
                     url(r'^category/(?P<category_name_slug>[\w\-]+)/$', myapp_views.category, name='category'),
                     url(r'prawne/$', myapp_views.Legal_inforamtion, name='prawne'),
                     url(r'^post/(?P<slug>[\w-]+)/$', myapp_views.post_detail, name='post_detail'),
                     url(r'^project/(?P<slug>[\w-]+)/$', myapp_views.projects_detail, name='project_detail'),
                     url(r'^restricted/$', myapp_views.restricted, name='restricted'),
                     url(r'^contact/$', myapp_views.contact, name='contact'),
                     url(r'^Messages/$', myapp_views.Messages, name='Messages'),
                     url(r'^message/(?P<pk>[0-9]+)/$',myapp_views.messages_detail, name='messages_details'),
                     url(r'^message/(?P<pk>[0-9]+)/delete(/yes)/$', myapp_views.message_deleting, name='messages_details'),
                     url(r'^postnew/$', myapp_views.Post_new, name='postnew'),
                     url(r'^post/(?P<pk>[0-9]+)/edit/$', myapp_views.postedit, name='postedit'),
                     url(r'^(?P<year>[0-9]{4})/$', myapp_views.PostYear.as_view(), name='postyear'),
                     url(r'^post/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',myapp_views.PostMonth.as_view(month_format='%m'), name='postmonth' ),
                     url(r'^projectsnew/$', myapp_views.projectsnew, name='projectsnew'),
                     url(r'^conceptions/$', myapp_views.conceptions, name='conceptions'),
                     url(r'^end_project/$', myapp_views.endproject, name='endproject'),
                     url(r'^progress_projects/$', myapp_views.progress_projects, name='progress_projects'),
                     url(r'^break_projects/$', myapp_views.break_projects, name='break_projects'),
]