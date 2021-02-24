from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('list/',views.ListArt.as_view()),
    path('buy/',views.RegisterCompra.as_view()),
    path('upload', views.FileView.as_view())

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)