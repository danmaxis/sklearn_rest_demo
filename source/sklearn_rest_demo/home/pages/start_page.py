from iommi import Table
from home.models import MLModel, MLModelType
from .common_page import CommonPage


class StartPage(CommonPage):
    type_table = Table(
        auto__model=MLModelType,
        title="Model Types",
        columns__created_at__include=False,
        columns__updated_at__include=False,
        columns__is_active__include=False,
        columns__is_deleted__include=False
        # auto__model_fields=['name', 'description'],
        )

    models_table = Table(
        auto__model=MLModel,
        title="Models",
        columns__created_at__include=False,
        columns__updated_at__include=False,
        columns__is_active__include=False,
        columns__is_deleted__include=False
        )

    class Meta:
        title = 'Start Page'
