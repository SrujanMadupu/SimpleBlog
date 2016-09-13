from django.conf.urls import url
from BlogMe import views

urlpatterns = [
    url('^create/',views.post_create),
    url('^(?P<slug>[\w-]+)/$',views.post_detail, name='detail'),
    url('^$',views.post_list,name='list'),
    url('^(?P<slug>[\w-]+)/edit/$',views.post_update,name='update'),
    url('^(?P<slug>[\w-]+)/delete/$',views.post_delete),
]

