"""
URL configuration for brickinator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import include, path

admin.site.site_header = "Brickinator Admin"
admin.site.site_title = "Brickinator Admin"
admin.site.index_title = "Brickinator Admin"

urlpatterns = [
    path('', include('landing.urls')),

    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/', include('accounts.urls')),
    
    path('app/profile/', include('user_profile.urls')),

    path('app/', include('dashboard.urls')),
    
    # Documentation for the project
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Generally, this should go last
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
