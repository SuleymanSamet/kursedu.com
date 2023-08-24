from django.urls import path
from . import views
from pages.views import IndexView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
