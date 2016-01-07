"""Pappy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, handler500, handler404
from django.contrib import admin
from events import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'register', views.UserView)
router.register(r'user', views.UserView)


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^events/', views.events, name='eventslist'),
  url(r'^admin/', admin.site.urls),
  url(r'^login/', views.LoginView.as_view(), name='login'),
]

urlpatterns += router.urls

handler404 = views.error404

handler500 = views.error500
