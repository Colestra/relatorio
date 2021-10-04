from django.urls import path
from .views import IndexView, Index2View

urlpatterns = [
    path('', IndexView.as_view(), name='inddex'),
    path('2/', Index2View.as_view(), name='index2'),
]