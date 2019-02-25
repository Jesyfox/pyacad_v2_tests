from django.urls import path, include
from django.conf.urls import url

from . import views, api_views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests/<int:test_id>', views.detail_of_test, name='detail_of_test'),
    path('tests/<int:test_id>/remove/<int:q_id>', views.remove_q, name='remove_q'),
    path('tests/<int:test_id>/add/<int:q_id>', views.add_q, name='add_q'),
    path('question/delete/<int:q_id>', views.delete_question, name='delete_question'),
    path('new_<str:new_object>', views.new_object, name='new_object'),
    path('tests/run_tests/<int:runtest_id>', views.run_test_detail, name='run_test_detail'),
    path('tests/notes/<int:test_id>', views.test_notes, name='test_notes'),
    path('tests/run_tests/notes/<int:runtest_id>', views.run_test_notes, name='run_test_notes'),
    path('tests/<int:test_id>/run', views.run_test, name='run_test'),
    path('user/logout', views.logout_view, name='logout'),
    path('user/signup', views.sign_up, name='signup'),
    path('user/login', views.login_view, name='login'),
    path('i18n/', include('django.conf.urls.i18n'), name='set_language'),
]


urlpatterns += [
    url(r'^question/$', api_views.QuestionList.as_view()),
    url(r'^question/(?P<pk>[0-9]+)/$', api_views.QuestionDetail.as_view()),
    url(r'^test/$', api_views.TestList.as_view()),
    url(r'^test/(?P<pk>[0-9]+)/$', api_views.TestDetail.as_view()),

]
