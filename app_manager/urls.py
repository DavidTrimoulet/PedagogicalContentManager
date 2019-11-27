from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # Bloom Verbs
    path('bloom_verbs/', BloomVerbView.as_view(), name="bloom_verb-all"),
    # Bloom levels
    path('bloom_levels/', BloomLevelView.as_view(), name="bloom_level-all"),
    # Bloom families
    path('bloom_families/', BloomFamilyView.as_view(), name="bloom_families-all"),
    # Bloom levels
    path('bloom_taxonomies/', BloomTaxonomyView.as_view(), name="bloom_taxonomies-all"),
    # Skill
    path('skill/', SkillView.as_view(), name="skill-all"),
    # Skill Rubricks
    path('skill_rubricks/', SkillRubricksView.as_view(), name="skill_rubricks-all"),
    # Problems
    path('problems/', ProblemsView.as_view(), name="problems-all"),
    # Version
    path('versions/', VersionView.as_view(), name="versions-all"),
    # Solution
    path('solutions/', SolutionView.as_view(), name="solutions-all"),
    # Validation
    path('hints/', HintView.as_view(), name="hints-all"),
    # Validation
    path('validations/', ValidationView.as_view(), name="validations-all"),
    # Validation
    path('hypothesis/', HypothesisView.as_view(), name="hypothesis-all"),
    # Image Upload
    path('uploadImage/', UploadImage.as_view(), name="upload-image")
]
