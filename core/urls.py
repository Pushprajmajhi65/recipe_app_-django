from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("aboutus/", home, name="home"),
    path("/contact", home, name="contact"),
    path('receipes', receipes, name="receipes"),
    path('login', login_page, name="login_page"),
    path('register', register_page, name="register_page"),

    # path('delete_receip/<id>', delete_receip, name="delete_receip"),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

