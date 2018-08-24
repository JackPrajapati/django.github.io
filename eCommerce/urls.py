from django.conf.urls import url,include
from django.contrib import admin
from .views import home_page,setting_page,about_page,contact_page,search
from django.conf import settings
from django.conf.urls.static import static	


urlpatterns = [
    url(r'^$', home_page, name="home_page"),
    url(r'^admin/', admin.site.urls),
    url(r'^setting/', setting_page, name="setting_page"),
    url(r'^contact/', contact_page, name="contact_page"),
    url(r'^about/', contact_page, name="about_page"),
    url( r'^search/', search, name = 'search' ),
    
    # Accounts app
    url(r'^accounts/', include('accounts.urls')),    
    
    # Products App
    url(r'^products/', include('products.urls')),

    # Products App
    url(r'^cart/', include('cart.urls')),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)