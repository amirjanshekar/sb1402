"""simulation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from maps.views import start_points
from maps.views import emergency_points
from maps.views import dangerous_points
from maps.views import ends_points
from maps.views import simul
from maps.views import traffic_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maps/startPoints', start_points),
    path('maps/emergencyPoints', emergency_points),
    path('maps/dangerousPoints', dangerous_points),
    path('maps/endPoints', ends_points),
    path('maps/simulation', simul),
    path('maps/traffic', traffic_path),
]
