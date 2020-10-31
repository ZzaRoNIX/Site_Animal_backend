"""AnimalSite URL Configuration

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
import Backend.views as views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/animals/create/$', views.excel_view),
    url(r'^api/animals/$', views.animal_list),
    # url(r'^api/animals/(?P<id>[0-9]+)$', views.animals_detail),
    # url(r'^api/orders/(?P<id>[0-9]+)$', views.order_detail)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
