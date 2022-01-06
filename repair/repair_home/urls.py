from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Home, Detail

urlpatterns = [
    path('', Home.as_view()),
    path('about_us', Home.as_view()),
    path('detail/<str:pk>', Detail.as_view(), name='product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
