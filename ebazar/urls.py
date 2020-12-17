"""ebazar URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib import admin
from emarket import views

admin.site.site_header = 'eBazar admin'
admin.site.site_title = 'eBazar admin'
# admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = 'eBazar administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^emarket/', include('emarket.urls'), name='emarket'),
    url(r'^SignUp/', views.create_user, name='sign_up'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'),  name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html', next_page='/'),  name='logout')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
