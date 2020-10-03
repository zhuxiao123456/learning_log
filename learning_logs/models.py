from django.db import models
from django.contrib.auth.models import User
#from __future__ import unicode_literals
# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #text是由字符或文本组成的数据，并设置固定长度，date_added记录日期和时间的数据，当用户创建新主题时，将属性设置成当前日期和时间
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
"""
为用户在学习笔记中添加的条目定义模型，每个条目都与特定主题相关联，这种关系被称为多对一关系，即多个条目可关联到同一个主题
外键是一个数据库术语，它引用了数据库中的另一条记录，下面的代码将每个条目关联到特定的主题，每个主题创建时都分配了一个键（或ID），需要数据联系时，使用键关联。
"""
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """返回模型的字符串表示，只让条目显示text的前50个字符，所以添加了省略号"""
        return self.text[:50] + "..."