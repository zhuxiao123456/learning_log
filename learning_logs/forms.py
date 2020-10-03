"""
创建表单的最简单方式是使用ModelForm,根据在上述定义的模型中的信息自动创建表单,最简单的ModelForm版本只含有一个内嵌的Meta类，告诉django根据哪个模型创建表单
以及在表单中含有哪些字段，根据Topic创建一个表单，以及在表单中包含text字段，labels让django不要为字段text生成标签
"""
from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = {'text'}
        labels = {'text':''}
"""
新类EntryForm继承了forms.ModelForm,它包含的Meta类指出了表单基于的模型以及要在表单中包含哪些字段，这里也给text指定了一个空标签
属性widgets，小部件widget是一个html表单元素，如单行文本框，多行文本区域或下拉列表，设置widgets可以覆盖django选择的默认小部件，宽度设置为80列而不是默认的40
"""
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}