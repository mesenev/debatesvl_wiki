from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from tabmaker_wiki import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include('django_nyt.urls')),
    path('', include('wiki.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
