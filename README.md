# NCER

基于`python3.6`和`Django2.1`的全国计算机等级考试刷题系统。

## 主要功能：
- 刷题
- 题库录入
## 目前集成：
二级python八百多道选择题，一百多道编程题
四级嵌入式开发工程师选择题库
### 配置
配置都是在`setting.py`中.部分配置迁移到了后台配置中。

很多`setting`配置我都是写在环境变量里面的.并没有提交到`github`中来.
## 运行

 修改`DjangoBlog/setting.py` 修改数据库配置，如下所示：

     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djangoblog',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': 3306,
        }
    }

### 创建数据库
mysql数据库中执行:
```sql
CREATE DATABASE `NCER` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
```
 然后终端下执行:

    ./manage.py makemigrations
    ./manage.py migrate
### 创建超级用户

 终端下执行:

    ./manage.py createsuperuser
### 创建测试数据
终端下执行:

    ./manage.py create_testdata
### 收集静态文件
终端下执行:  

    ./manage.py collectstatic --noinput
    ./manage.py compress --force
### 开始运行：
 执行：
 `./manage.py runserver`





 浏览器打开: http://127.0.0.1:8000/  就可以看到效果了。
