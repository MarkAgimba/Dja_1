from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.main_gallery,name = 'main_gallery'),
    # path('location/',views.location,name = 'location'),
    path('searchh/',views.search,name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
