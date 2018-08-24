from django.conf.urls import url,include
from cart.views import mycart

app_name="cart"

urlpatterns = [
    url(r'^$', mycart, name="cart_home"),
    ]