from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from scraper import views as ebooks_views

urlpatterns = [
    path('', ebooks_views.home, name='home'),
    path('search/', ebooks_views.search, name='search'),
    path('about/', ebooks_views.about, name='about'),
    path('policy/', ebooks_views.policy, name='policy'),
    path('contact/', ebooks_views.contact_us, name='contact'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
