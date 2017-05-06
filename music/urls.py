from django.conf.urls import url
from . import views


app_name = 'music'

urlpatterns = [
	# /music/
   url(r'^$', views.index, name='index'),

   # /music/*some_album_id*/
   url(r'^(?P<album_id>\d+)/$', views.detail, name='detail'),

   # /music/*some_album_id*/favorite/
   url(r'^(?P<album_id>\d+)/favorite/$', views.favorite, name='favorite'),
]