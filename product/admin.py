from django.contrib import admin
from django.apps import apps

# Register your models here.

product_models = apps.get_app_config('product').get_models()

for model in product_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
