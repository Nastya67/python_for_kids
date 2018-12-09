from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('main', views.main, name='main'),
    url('logout', views.log_out, name='logout'),
    url('new_group', views.new_group, name='new_group'),
    url('del_group', views.del_group, name='del_group'),
    url('tables', views.table, name='tables'),
    url('table_(?P<group_id>.+)', views.table_s, name='table_s'),
    url('settings', views.settings, name='settings'),
    url('lvl(?P<lvl_id>\d+)', views.level, name='level'),
    url("submit(?P<lvl_id>\d+)", views.get_answer, name="submit"),
    url("run(?P<lvl_id>\d+)", views.get_result, name="run"),
]
