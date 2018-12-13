from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
        url(r'^$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
        url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        #url(r'^logout/$', auth_views.LogoutView.as_view(template_name=template_name), name='logout'),
]
