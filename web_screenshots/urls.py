from django.conf.urls import url
from django.contrib import admin
from screenshots.views import landing

urlpatterns = [
	url(r'^$', landing, name='landing'),
    url(r'^admin/', admin.site.urls),
]
