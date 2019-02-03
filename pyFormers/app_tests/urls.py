from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>', views.category_detail, name='category_detail')
]