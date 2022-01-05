from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, Home, Detail

urlpatterns = [
    path('', index),
    # path('delivery', )
    # path('products', products)
    path('about_us', Home.as_view()),
    path('detail/<str:pk>', Detail.as_view(), name='product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
