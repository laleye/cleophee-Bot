from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.home),
    #url(r'^chat/cs/', views.cs),
    #url(r'^chat/download/', views.download),
    #url(r'^chat/speech/', views.speech),
    #url(r'^chat/v_reponse/', views.v_reponse),
]

