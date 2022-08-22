from django.contrib import admin
from home.models import MLModel, MLModelType


# Register your models here.
admin.site.register(MLModel)
admin.site.register(MLModelType)
