from django.urls import path, re_path

from . import views
from .views import ElectronicsView
from django.conf.urls import include
import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('', views.index, name='index'),
    re_path(r'^\d+', views.detail, name='detail'),
    # re_path(r'^electronics', views.electronics, name='electronics')
    # re_path(r'^electronics', ElectronicsView.as_view(), name='electronics'),
    re_path(r'^electronics', ElectronicsView.as_view(), name='electronics'),
    re_path(r'^logout', views.logout, name='logout')
]