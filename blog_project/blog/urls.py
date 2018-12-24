from django.conf.urls import url
from blog import views

urlpatterns = [

    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post'),  # its grab a PK and get all his info
    url(r'post/new/$', views.CreatePostView.as_view(), name='post_new')  # go to PostForm
]
