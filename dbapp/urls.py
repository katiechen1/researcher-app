"""dbapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from researchers import views 
# from collection import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'researchers/(\d+)/', views.researcher_detail, name='researcher_detail'),
    url(r'^nominate/$', views.nominate, name='nominate'),
    url(r'^nomineeinfo/$', views.nominee_info, name='nominee_info'),
    # url(r'register/$', views.register_user, name='register_user'),
    url(r'about/$', views.about, name='about'),
    url(r'nomthanks/$', views.nomthanks, name='nomthanks'),
    url(r'feedback_thanks/$', views.feedback_thanks, name = 'feedback_thanks'),
    url(r'thanks/$', views.thanks, name='thanks'),
    url(r'nombadinfo/$', views.nombadinfo, name='nombadinfo'), 
    url(r'badinfo/$', views.badinfo, name='badinfo'), 
    url(r'feedback/$', views.feedback, name='feedback'),
    url(r'alreadyexists/$',views.alreadyexists,name='alreadyexists')]
