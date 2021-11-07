from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import Homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homeview.as_view(), name="home"),
    path('blog/', include('blog.urls', namespace="blog"))
]