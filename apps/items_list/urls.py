from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list$', views.results),
    url(r'^results$', views.showList),
    url(r'^go/back$', views.back),
]