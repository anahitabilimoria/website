# -*- coding: utf-8 -*-
from django.urls import path
from django.conf.urls import url



from . import views
urlpatterns = [
	path("",views.index),
	url(r"^index/$",views.index, name = "index"),
	url(r"^editView/(?P<PID>\d+)/$",views.editView, name = "editView"),
	url(r"^createPerson/$",views.createPerson, name = "createPerson"),
	url(r"^delete_person/(?P<ID>\d+)/$", views.delete_person, name="delete_person"),
	url(r"^uploadView/$", views.uploadView, name = "uploadView")
]