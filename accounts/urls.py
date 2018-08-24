from django.conf.urls import url
from .views import login_page,register_page,logout_page
from .views import register_page
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    
    url(r'^login/', login_page, name="login_page"),
    url(r'^register/', register_page, name="register_page"),
    url(r'^logout/', logout_page, name="logout_page"),
    url(r'^profile/', logout_page, name="profile_page"),
]
