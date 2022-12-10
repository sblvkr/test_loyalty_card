from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('card.urls', namespace='card')),
    path('admin/', admin.site.urls),
]
