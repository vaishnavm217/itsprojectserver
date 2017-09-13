"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from api import views 

urlpatterns = [
    	url(r'^households/',views.snippet_list1),
	url(r'^members/',views.snippet_list2),
	url(r'^photos/',views.snippet_list3),
	url(r'^videos/',views.snippet_list4),
	url(r'^farms/',views.snippet_list5),
	url(r'^crops/',views.snippet_list6),
	url(r'^wells/',views.snippet_list7),
	url(r'^wellwater/',views.snippet_list8),
    url(r'^housedat/(?P<dat_id>[0-9]+)/',views.Housew),
]
