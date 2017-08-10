"""assessment URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from api.views import FileViewSet
router = routers.DefaultRouter()
router.register(r'^file',FileViewSet)


schema_view = get_swagger_view(title='File upload APi')

urlpatterns = [

]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api_auth/',include('rest_framework.urls', namespace="rest_framework")),
    url(r'^',include(router.urls)),
    url(r'^help', schema_view),
]
# Add media paths to urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)