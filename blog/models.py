from django.db import models
from django.contrib.auth.models import  User
from DjangoUeditor.models import UEditorField
# 导入Django自带的用户模块
# Create your models here.

# 文章分类
class ArticleKind(models.Model):
    name = models.CharField("博客分类", max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章标签
class ArticleTag(models.Model):
    name = models.CharField('文章标签', max_length=100)
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 推荐位
class Recommend(models.Model):
    name = models.CharField('推荐位', max_length=100)
    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    kind = models.ForeignKey(ArticleKind, on_delete=models.DO_NOTHING,
                             verbose_name='分类', blank=True, null=True)
    tags = models.ManyToManyField(ArticleTag, verbose_name='标签', blank=True)
    img = models.ImageField('文章图片',upload_to='article_img/', null=True)
    # content = models.TextField()
    content = UEditorField('内容', width=800, height=500,
                           toolbars='full', imagePath='upimg/', filePath='upfile/',
                           upload_settings={'imageMaxSize': 1204000
                           },settings={},command=None, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    # """
    #      文章作者，这里User是从django.contrib.auth.models导入的。
    #      这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # """
    viewscount = models.PositiveIntegerField('阅读量', default=0)
    recommend = models.ForeignKey(Recommend, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    created_time =  models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    def __str__(self):
        return self.title

# Banner
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='media/banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否activce', default=False)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text_info

# 友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址', max_length=100)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name