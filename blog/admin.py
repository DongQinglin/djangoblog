from django.contrib import admin
from .models import Banner, ArticleTag, ArticleKind, Article, Link, Recommend
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 添加想要展示的字段
    list_display = ('id', 'kind', 'title', 'recommend', 'author', 'viewscount', 'created_time')
    list_per_page = 50
    ordering = ('created_time',)
    # 后台编辑
    list_display_links = ('id', 'title')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(ArticleKind)
class ArticleKindAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')