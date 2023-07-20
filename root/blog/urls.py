#from django.conf.urls import url
from django.urls import path
from .views import PostList, post_detail

urlpatterns = [
       path('', PostList.as_view(), name='blog_post_list'), # η view είναι class based view
       path('<slug:slug>/', post_detail, name='blog_post_detail'),
       #path('', post_list, name='blog_post_list'), # η view είναι function view
       # re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[-\w]+)/$', post_detail, name='blog_post_detail')
       # re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$', post_detail, name='blog_post_detail'),
]