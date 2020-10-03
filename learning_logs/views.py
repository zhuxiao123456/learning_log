from django.shortcuts import render
from .models import Topic,Entry
from django.urls import reverse
from django.http import HttpResponseRedirect,Http404
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
#django使用了装饰器@login_required限制访问，对于某些页面只允许允许已登陆的用户访问它们，装饰器（decorator）是放在函数定义前面的指令
# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')
#加上@login_required之后，让python运行topics()的代码前先运行login_required的代码
#login_required的代码检查用户是否已经登陆，仅当用户登录时，django才运行topics的代码，如果用户未登陆，就重定向到登陆页面
@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    #topics = Topic.objects.order_by('date_added') #查询数据库，请求提供Topic对象，并按属性data_added对他们进行排序
    context = {'topics':topics} #定义了一个将要发送给模板的上下文，为字典
    return render(request,'learning_logs/topics.html',context)
@login_required
def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    #这个代码称为查询，向数据库查询特定的信息
    return render(request,'learning_logs/topic.html',context)
@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据，创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    #函数reverse根据制定的URL模型确定URL，意味着django将在页面被请求时生成URL
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:#post提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)
@login_required
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id) #获取用户要修改的的条目对象，以及与该条目相关的主题
    topic = entry.topic
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)#让django创建一个表单，并使用既有条目对象中的信息填充它，用户将看到既有的数据并编辑他们
    else:
        # POST提交的数据，对数据进行处理，传递着两个实参，让django根据既有条目对象创建一个表单实例，并根据requese.POST中的相关数据进行修改
        # 然后检查表单是否有效，如果有效，就调用save,然后重新定向到显示条目所属主题的页面，用户将在其中看到其编辑的条目的新版本
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)














