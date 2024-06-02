from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, DetailView

urlpatterns = [
    path('api/docs/', DetailView.as_view(template_name='redoc.html'), name='redoc'),
    path('api/', include('users.urls')),
    path('admin/', admin.site.urls),
]
