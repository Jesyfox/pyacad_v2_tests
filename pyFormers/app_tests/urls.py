from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests/<int:test_id>', views.detail_of_test, name='detail_of_test'),
    path('question/delete/<int:q_id>', views.delete_question, name='delete_question'),
    path('new_<str:new_object>', views.new_object, name='new_object'),
]