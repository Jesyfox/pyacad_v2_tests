from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:test_id>', views.test_detail, name='test_detail')
]