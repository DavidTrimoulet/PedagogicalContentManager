from django.urls import path

from . import views
from .views import BloomVerbView, BloomVerbDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('bloom_verbs/', BloomVerbView.as_view(), name="bloom_verb-all"),
    path('bloom_verbs/<int:pk>/', BloomVerbDetailView.as_view(), name="bloom_verb-detail")
]
