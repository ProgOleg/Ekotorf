"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'Ekotorf.menu.CustomMenu'
"""

try:
    from django.urls import reverse
except ImportError:
    pass
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu

class MyMenu(Menu):
    def __init__(self, **kwargs):
        super(MyMenu, self).__init__(**kwargs)
        self.children += [
            items.MenuItem('Home', reverse('admin:index')),
            items.AppList('Applications'),
            items.MenuItem('Multi level menu item',
                children=[
                    items.MenuItem('Child 1', '/foo/'),
                    items.MenuItem('Child 2', '/bar/'),
                ]
            ),
        ]



class CustomMenu(Menu):
    """
    Custom Menu for Ekotorf admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.Bookmarks(),
            items.AppList(
                _('Applications'),
                exclude=('django.contrib.*',)
            ),
            items.AppList(
                _('Administration'),
                models=('django.contrib.*',)
            ),
            items.MenuItem('Стили',
                           children=[

                           ]),
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)