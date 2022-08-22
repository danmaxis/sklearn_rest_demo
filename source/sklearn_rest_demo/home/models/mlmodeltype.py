from django.db import models
from home.models.common_model import CommonModel


class MLModelType(CommonModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'ML Model Type'
        verbose_name_plural = 'ML Model Types'
