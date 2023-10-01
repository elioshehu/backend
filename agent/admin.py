from django.contrib import admin
from django.apps import apps

# Register your models here.

agent_models = apps.get_app_config('agent').get_models()

for model in agent_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
