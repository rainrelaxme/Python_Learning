# 学习Django
使用Django，首先需要建立一个虚拟工作环境。虚拟环境 是系统的一个位置，你可以在其中安装包，并将其与其他Python包隔离。将项目的库与其他项目分离是有益的，且为
了在第20章将“学习笔记”部署到服务器，这也是必须的。

* 建立虚拟环境：python -m venv ll_env
* 激活虚拟环境
  * linux：source ll_env/bin/activate ；
  * Windows：ll_env\Scripts\activate ；
* 停止使用虚拟环境，可执行命令deactivate
*  安装django：pip install Django
* 创建项目 django-admin.exe startproject learing_log .
* 创建数据库python manage.py migrate:会创建dbsqlite3数据库
* 查看项目python manage.py runserver <端口号>
* 创建应用程序：python manage.py startapp learning_logs
  * <learning_logs>:appname
* 修改模型：models.py
  * django模型中使用的字段介绍：https://docs.djangoproject.com/en/1.8/ref/models/fields/
* 每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤：
  * 修改models.py；
  * 对learning_logs 调用makemigrations ；<python manage.py makemigrations learning_logs>
  * 让Django迁移项目。<python .\manage.py migrate">