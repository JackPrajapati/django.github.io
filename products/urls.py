from django.conf.urls import url
from . import views

app_name = 'products'

urlpatterns = [

    url(r'^product_list/$', views.product_list, name="product_list"),
    url(r'^product_details/(?P<pk>\d+)/$', views.product_details, name="product_details"),
]