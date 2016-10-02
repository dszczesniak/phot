"""projectphoto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from photoapp.views import *
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),
    url(r'^kontakt/$', contact, name='kontakt'),
    url(r'^o_mnie/$', me, name='o_mnie'),
    url(r'^portfolio/$', portfolio, name='portfolio'),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^sesje_ciazowe/$', sessions_pregnancy_view, name='sesje_ciazowe'),
    url(r'^sesje_rodzinne/$', sessions_family_view, name='sesje_rodzinne'),
    url(r'^sesje_noworodkowe/$', sessions_neonatal_view, name='sesje_noworodkowe'),
    url(r'^sesje_okazjonalne/$', sessions_occasional_view, name='sesje_okazjonalne'),
    url(r'^projekt_360/$', project_360_view, name='projekt_360'),
    
    ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
                    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)