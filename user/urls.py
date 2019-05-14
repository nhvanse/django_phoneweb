from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^logout/$', views.logout_view, name='logout'),
]