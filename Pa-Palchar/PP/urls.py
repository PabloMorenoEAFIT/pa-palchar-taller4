"""PP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from eventos import views as eventoVista
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', eventoVista.home, name='home'),
    path('<int:year>/<str:month>/', eventoVista.home),
    path('eventos', eventoVista.all_events, name="eventlist"),
    path('addvenue',eventoVista.addvenue, name='addvenue'),
    path('venue',eventoVista.venues, name='venue'),
    path('show_venue/<venue_id>',eventoVista.show_venues, name='show_venue'),
    path('show_event/<event_id>',eventoVista.show_events, name='show_event'),
    path('search_result',eventoVista.search_result, name='search_result'),
    path('update_venue/<venue_id>', eventoVista.update_venue, name='update_venue'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
