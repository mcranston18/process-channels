from django.conf.urls import url
from django.contrib import admin

from processes.views import HomeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
]
