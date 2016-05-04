from django.conf.urls import url
from django.contrib import admin

from .views import (
	PostListApiView,
	PostDetailAPIView,
	PostUpdateAPIView,
	PostDeleteAPIView,
	PostCreateAPIView,
	create_api,
	home,
	)

urlpatterns = [
    # url(r'^pincode/$', views.get_courier_details, name='get_courier_details'),
   	# url(r'^home/$', views.home, name='home'),
   	url(r'^$', PostListApiView.as_view(), name='list'),
   	url(r'^(?P<pk>\d+)$', PostDetailAPIView.as_view(), name='detail'),
   	url(r'^(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
   	url(r'^(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
   	url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
   	url(r'^available/$', create_api, name='available'),
   	url(r'^home/$', home, name='home'),

]