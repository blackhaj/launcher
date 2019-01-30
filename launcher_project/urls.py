# launcher_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('controlpanel/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')), # new
]