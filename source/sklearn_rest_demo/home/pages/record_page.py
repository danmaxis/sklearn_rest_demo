from iommi import Form
from home.models import MLModel, MLModelType
from .common_page import CommonPage


class RecordsPage(CommonPage):
    create_modeltype = Form.create(
        auto__model=MLModelType,
        auto__exclude=['id', 'created_at', 'updated_at', 'is_active', 'is_deleted'],
        )
    
    create_model = Form.create(
        auto__model=MLModel,
        auto__exclude=['id', 'created_at', 'updated_at', 'is_active', 'is_deleted'],
        )

    class Meta:
        title = 'Add Records Page'
