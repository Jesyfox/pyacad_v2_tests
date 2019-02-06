from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests/<int:test_id>', views.detail_of_test, name='detail_of_test'),
    path('tests/<int:test_id>/remove/<int:q_id>', views.remove_q, name='remove_q'),
    path('tests/<int:test_id>/add/<int:q_id>', views.add_q, name='add_q'),
    path('question/delete/<int:q_id>', views.delete_question, name='delete_question'),
    path('new_<str:new_object>', views.new_object, name='new_object'),
]