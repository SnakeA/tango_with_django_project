__author__ = 'snake'

from django.conf.urls import patterns, url # machinery to create url mappings
from rango import views #touta en ta views mas

# we use tuple to create them. CALLED urlpatterns
# ^$ simenei Empty String
# Any URL supplied by the user that matches this pattern means that the view views.index() would be invoked by Django
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))