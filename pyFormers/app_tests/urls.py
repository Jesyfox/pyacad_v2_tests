from django.urls import path, include
from django.conf.urls import url

from . import views, api_views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/delete/<int:q_id>', views.delete_question, name='delete_question'),
    path('new_<str:new_object>', views.new_object, name='new_object'),

    path('tests/<int:test_id>/remove/<int:q_id>', views.remove_q, name='remove_q'),
    path('tests/<int:test_id>/add/<int:q_id>', views.add_q, name='add_q'),

    path('tests/<int:test_id>', views.detail_of_test, name='detail_of_test'),
    path('tests/<int:test_id>/edit', views.edit_test, name='edit_test'),
    path('tests/<int:test_id>/delete', views.test_delete, name='delete_test'),
    path('tests/<int:test_id>/run', views.run_test, name='run_test'),
    path('tests/run_tests/<int:runtest_id>', views.run_test_detail, name='run_test_detail'),

    path('<str:model_object>/<int:obj_id>/notes/', views.model_notes, name='model_notes'),

    path('user/logout', views.logout_view, name='logout'),
    path('user/signup', views.sign_up, name='signup'),
    path('user/login', views.login_view, name='login'),

    path('i18n/', include('django.conf.urls.i18n'), name='set_language'),
]


urlpatterns += [
    url(r'^rest/questions/$', api_views.QuestionViewSet.as_view({'get': 'list'})),
    url(r'^rest/questions/(?P<pk>[0-9]+)/$', api_views.QuestionViewSet.as_view({'get': 'retrieve'})),
    url(r'^rest/questions/create/$', api_views.QuestionViewSet.as_view({'post': 'create'})),

    url(r'^rest/tests/$', api_views.TestViewSet.as_view({'get': 'list'})),
    url(r'^rest/tests/(?P<pk>[0-9]+)/$', api_views.TestViewSet.as_view({'get': 'retrieve'})),
    url(r'^rest/tests/create/$', api_views.TestViewSet.as_view({'post': 'create'})),

    url(r'^rest/run_tests/$', api_views.RunTestViewSet.as_view({'get': 'list'})),
    url(r'^rest/run_tests/(?P<pk>[0-9]+)/$', api_views.RunTestViewSet.as_view({'get': 'retrieve'})),
    url(r'^rest/run_tests/create/$', api_views.RunTestViewSet.as_view({'post': 'create'})),

    url(r'^rest/notes/$', api_views.NotedItemViewSet.as_view({'get': 'list'}))
]
