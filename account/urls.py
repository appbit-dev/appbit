from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^edit-profile$', views.edit_profile, name='edit_profile'),
]
