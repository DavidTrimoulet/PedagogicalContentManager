from django.contrib import admin
from django.apps import apps

models = apps.get_app_config('app_manager').get_models()

for model in models:
    admin.site.register(model)
    #@admin.register(model)
