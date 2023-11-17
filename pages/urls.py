from django.urls import path
from pages.views import index,about

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='index'),
    path('about',about,name="about"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)