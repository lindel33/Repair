from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CheckNoteBook

urlpatterns = [
    path('/check', CheckNoteBook.as_view()),
    # path('/search_okey', CheckNoteBookOk.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
