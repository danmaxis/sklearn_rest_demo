

from iommi import Menu, MenuItem, Page


class CommonPage(Page):
    menu = Menu(
        sub_menu=dict(
            start=MenuItem(display_name='Home', url='/start/'),
            records=MenuItem(display_name='Add Records', url='/records/'),
        ),
    )