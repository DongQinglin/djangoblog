from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, ArticleKind, Banner, Link, Recommend,ArticleTag
# Create your views here.

def hello(request):
    return HttpResponse('欢迎使用Django！')
# 首页
def index(request):
    # 取出分类

    allArticleKind = ArticleKind.objects.all()
    # print(allArticleKind)
    banner = Banner.objects.filter(is_active=True)[0:4]
    # print(banner)
    recommend = Article.objects.filter(recommend=1)[:3]
    # print(recommend)
    tags = ArticleTag.objects.all()
    # print(tags)
    rightRecmmend = Article.objects.filter(recommend=2)[:6]
    # print(rightRecmmend)
    allArticle = Article.objects.all().order_by('-id')
    print("-----", allArticle[0])
    hot = Article.objects.all().order_by('-viewscount')  # 通过浏览数进行排序
    # print(hot)
    links = Link.objects.all()
    # print(links)
    context = {
        'allArticleKind': allArticleKind,
        'banner': banner,
        'recommend': recommend,
        'allArticle': allArticle,
        'hot': hot,
        'rightRecmmend': rightRecmmend,
        'tags': tags,
        'links': links,
    }
    return render(request, 'index.html', context)

    # return HttpResponse('hello')
    # return render(request, 'base.html', context)
    # 添加两个变量
    # sitename = '元青的法律学习笔记'
    # url = 'www.fabaoer.cn'
    # # 新加一个列表
    # lists = [
    #     '开发前的准备',
    #     '项目需求分析',
    #     '数据库设计分析',
    #     '创建项目',
    #     '基础配置',
    #     '欢迎页面',
    #     '创建数据库模型',
    # ]
    # # 在来的基础上新加一个字典
    # mydict = {
    #     'name': '董庆林',
    #     'qq': '1745509482',
    #     'wx': '18336126797',
    #     'email': '1745509482@qq.com',
    # }
    # allArticle = Article.objects.all()
    #
    #
    # context = {
    #     # 'sitename': sitename,
    #     # 'url': url,
    #     # 'lists':lists,
    #     # 'mydict':mydict,
    #     'allArticle': allArticle,
    # }
    # return render(request, 'index.html', context)
# 列表页
def list(request, lid):
    list = Article.objects.filter(kind_id=lid)  # 获取通过URL传进来的lid，然后筛选出对应文章
    cname = ArticleKind.objects.get(id=lid)  # 获取当前文章的栏目名
    remen = Article.objects.filter(recommend_id=2)[:6]  # 右侧的热门推荐
    allcategory = ArticleKind.objects.all()  # 导航所有分类
    tags = ArticleTag.objects.all()  # 右侧所有文章标签

    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'list.html', locals())
    # return HttpResponse('hello')

# 内容页
def show(request, sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allArticleKind = ArticleKind.objects.all()  # 导航上的分类
    tags = ArticleTag.objects.all()  # 右侧所有标签
    remen = Article.objects.filter(recommend__id=2)[:6]  # 右侧热门推荐
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, kind=show.kind.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, kind=show.kind.id).last()
    show.viewscount = show.viewscount + 1
    show.save()
    return render(request, 'show.html', locals())

# 标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)  # 通过文章标签进行查询文章

    remen = Article.objects.filter(recommend__id=2)[:6]
    allAtricleKind = ArticleKind.objects.all()
    tname = ArticleTag.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    tags = ArticleTag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())

# 搜索页
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)  # 获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(recommend__id=2)[:6]
    allArticleKind = ArticleKind.objects.all()
    page = request.GET.get('page')
    tags = ArticleTag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())

# 关于我们
def about(request):
    allArticleKind = ArticleKind.objects.all()
    return render(request, 'page.html', locals())
