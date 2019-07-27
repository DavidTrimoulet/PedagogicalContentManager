from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    # Bloom Verbs
    path('bloom_verbs/', BloomVerbView.as_view(), name="bloom_verb-all"),
    path('bloom_verbs/<int:pk>/', BloomVerbDetailView.as_view(), name="bloom_verb-detail"),
    # Bloom levels
    path('bloom_levels/', BloomLevelView.as_view(), name="bloom_level-all"),
    path('bloom_levels/<int:pk>/', BloomLevelDetailView.as_view(), name="bloom_Level-detail"),
    # Bloom levels
    path('bloom_taxonomy/', BloomTaxonomyView.as_view(), name="bloom_taxonomy-all"),
    path('bloom_levels/<int:pk>/', BloomTaxonomyDetailView.as_view(), name="bloom_taxonomy-detail")
]
