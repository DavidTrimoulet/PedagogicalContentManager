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
    path('bloom_levels/<int:pk>/', BloomLevelDetailView.as_view(), name="bloom_level-detail"),
    # Bloom families
    path('bloom_families/', BloomFamilyView.as_view(), name="bloom_families-all"),
    path('bloom_families/<int:pk>/', BloomFamilyDetailView.as_view(), name="bloom_families-detail"),
    # Bloom levels
    path('bloom_taxonomies/', BloomTaxonomyView.as_view(), name="bloom_taxonomies-all"),
    path('bloom_taxonomies/<str:verb>/', BloomTaxonomyDetailView.as_view(), name="bloom_taxonomies-detail"),
    # Skill
    path('skill/', SkillView.as_view(), name="skill-all"),
    path('skill/<str:verb>/', SkillDetailView.as_view(), name="skill-detail"),
    # Skill Rubricks
    path('skill_rubricks/', SkillRubricksView.as_view(), name="skill_rubricks-all"),
    path('skill_rubricks/<str:verb>/<str:text>', SkillRubricksDetailView.as_view(), name="skill_rubricks-detail")
]
