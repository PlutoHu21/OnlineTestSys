# OnlineTestSys
在线习题测试平台。

后端基于Python的Django框架，后台使用SampleUI，前端基于Bootstrap。

安装所需框架:

	pip install -r requirement.txt

下载后需要重新迁移数据库：

	py manage.py makemigrations
	py manage.py migrate

启动：

	py manage.py runserver 80

访问网页：

```
127.0.0.1:8000
```

创建管理员：

	py manage.py createsuperuser

访问后台：

```
127.0.0.1:8000/admin
```

