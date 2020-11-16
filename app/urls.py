from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexPage.as_view(), name='index_pg'),

    path('application/', application_view, name='application_url'),
    path('feedback/', feedback_view, name='feedback_url'),
    path('callback/', callback_view, name='callback_url'),
    path('mailing/', mailing_view, name='mailing_url'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
