"""
定义learning_logs的URL模式
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url,re_path
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^$',views.index,name='index'),#r'^$'这是个正则表达式，让python查找开头和末尾之间没有任何东西的URL，其他的都不是互相匹配的
    path('',views.index,name='index'),
    #re_path('^topic/$',views.topics,name='topics'),
    #path('topics/',views.topics,name='topics'),
    path('topics/', views.topics, name='topics'),
    path("topics/(?P<topic_id>\d+)/", views.topic, name='topic'),
    # 运用了正则表达式，表达式两边的括号捕获URL中的值，?P<topic_id>将匹配的值存储到topic_id中，\d+与包含在斜杠内的任何数字都匹配，不管为多少位
    # 发现URL匹配时。将调用视图函数topic,并将存储在topic_id中的值作为实参传递给他，使用topic_id的值获取相应的主题
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/(?P<topic_id>\d+)/',views.new_entry,name='new_entry'),#用于添加新条目的页面
    #在用于添加新条目的页面的URL模式中，需要包含实参topic_id,因为条目必须与特定的主题相关联
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),#用于编辑条目的页面
]
