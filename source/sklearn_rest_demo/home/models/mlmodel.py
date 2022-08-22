from django.db import models
from home.models.common_model import CommonModel


class MLModel(CommonModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    model = models.TextField()
    model_type = models.ForeignKey('MLModelType', on_delete=models.PROTECT)
    parameters = models.TextField()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'ML Model'
        verbose_name_plural = 'ML Models'
