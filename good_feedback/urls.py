from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("project.urls")),
    path("account/", include("account.urls")),
    path("feedback/", include("feedback.urls")),
]
