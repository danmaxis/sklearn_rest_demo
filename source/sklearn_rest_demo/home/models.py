from django.db import models

class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


# Create your models here.
class MLModel(CommonModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    model = models.TextField()
    model_type = models.ForeignKey('MLModelType', on_delete=models.PROTECT)
    parameters = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'ML Model'
        verbose_name_plural = 'ML Models'

class MLModelType(CommonModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'ML Model Type'
        verbose_name_plural = 'ML Model Types'