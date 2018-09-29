from django.conf.urls import include, url
import FirstDjangoApp.views

urlpatterns = [
    url(r'^$', FirstDjangoApp.views.index, name='index'),
    url(r'^home$', FirstDjangoApp.views.index, name='home'),
]
