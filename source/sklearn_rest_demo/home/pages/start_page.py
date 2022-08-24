from iommi import Asset, Table, html
from home.models import MLModel, MLModelType
from .common_page import CommonPage


class StartPage(CommonPage):
    d3_import = Asset.js(
        attrs__charset='utf-8',
        attrs__src='https://d3js.org/d3.v5.min.js',
    )

    c3_import = Asset.js(
        attrs__src='https://cdnjs.cloudflare.com/ajax/libs/c3/0.7.0/c3.min.js',
    )

    # Load chart file from static folder
    chart_file = Asset.js(
        attrs__type='module',
        attrs__src='../static/js/graph.js',
    )

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

    graph_area = html.div(
        attrs__id='graph_area',
        attrs__width='200px',
        attrs__height='200px',
    )

    

    class Meta:
        title = 'Start Page'
