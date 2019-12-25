# python_django_websit

This is a blog project product by python Django.
这一项目使用python Django实现。主要经验来源于Django中文社区。
## 搭建运行环境

- git 版本控制，为了能拉到服务器上。

        `$ git init // 初始化git本地仓库
        `$ touch .gitignore // 创建git忽略文件

> 忽略文件的内容暂时定为`/venv`，即虚拟环境被忽略。        
        
- django安装，框架准备

        `$ pip3 install django // 安装django
        >>> import django //导入django
        >>> print(django.get_version()) // 获取版本号

- 验证django版本

        `$ python3 -m django --version
        3.0 // 注意这里是python3
- 创建django项目

        `venv`$ django-admin startproject djangoblog
        
- django运行
        
        `$ python3 manage.py runserver

- django创建app页面

        `$ python3 manage.py startapp blog 
        
- `setting`主配置文件

        // 设置域名访问权限
        myblog/settings.py
        ALLOWED_HOSTS = []      #修改前
        ALLOWED_HOSTS = ['*']   #修改后，表示任何域名都能访问。如果指定域名的话，在''里放入指定的域名即可
       
        // 添加模板目录templates的路径
        #修改前
        'DIRS': []
        #修改后
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        注：使用pycharm创建的话会自动添加
        
        // 使用默认的sqlite
        // 注册blog app
        'blog.apps.BlogConfig', # 注册APP应用
        
        // 修改项目语言和时区
        #修改前为英文
        LANGUAGE_CODE = 'en-us'
        #修改后
        LANGUAGE_CODE = 'zh-hans' #语言修改为中文
        #时区，修改前
        TIME_ZONE = 'UTC'
        #修改后
        TIME_ZONE = 'Asia/Shanghai' #
        
        // 在项目根目录里创建static和media，两个目录。static用来存放模板CSS、JS、图片等静态资源，media用来存放上传的文件，后面我们在讲解数据库创建的时候有说明
        #设置静态文件目录和名称
        STATIC_URL = '/static/'

        #加入下面代码

        #这个是设置静态文件夹目录的路径
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
        )
        #设置文件上传路径，图片上传、文件上传都会存放在此目录里
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        
- 数据库迁徙

        `$ python3 manage.py makemigrations
        `$ python3 manage.py migrate
        
        // 创建管理员密码
        `$ python3 manage.py createsuperuser
        

- 设计数据表

|名称|英文名|作用
|--|--|--|
文章|article|文章表
文章分类|article_kind|1:m文章
文章标签|article_tag|m:n文章

- 文章表

列名|英文名
--|--
标识|id
文章标题|title
作者|athuor
摘要|excerpt
分类|kind： article_kind
标签|tag： article_tag
内容|content
创建时间|created_time
推荐|recommend
封面图片|banner

- git提交

        `$ git init
        `$ git add .
        `$ git commit -m 'A blog first commit.'
        `$ git remote -v
        `$ git remote set-url origin URL
        `$ git remote add origin ...git
        `$ git stash
        
        `$ git pull --rebase origin master
        `$ git push -u origin master
        
- 部署服务器
                        
        netstat -npta | grep 22 // 查看端口线程
        sudo /etc/init.d/nginx start // 启动nginx
        sudo lsof -i:端口号 // 根据端口查找进程
        sudo kill PID号
        
- 屏幕适配

        
          <meta name="viewport" content="viewport-fit=cover, width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
          <meta name="format-detection" content="telephone=no" />
          <meta name="msapplication-tap-highlight" content="no" />


          <!-- add to homescreen for ios -->
          <meta name="apple-mobile-web-app-capable" content="yes" />
          <meta name="apple-mobile-web-app-status-bar-style" content="black" />
          
- 进程保留

        screen -S  blog
        screen -S session_name -X quit
        ctrl+d
        screen -ls

