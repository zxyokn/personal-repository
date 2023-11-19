# flask

- ```py
  from flask import Flask
  
  app = Flask(__name__)
  
  
  @ app.route('/')
  def helloworld():
      return "hello world!"
  
  
  if __name__== '__main__':
      app.run()
  ```

  ### debug,host和port修改
  
  - ```py
    from flask import Flask
    
    app = Flask(__name__)
    
    # 创建根路由和视图函数的映射
    @ app.route('/')
    def helloworld():
        return "hello world!"
    
    # 1. debug模式
    # 开启debug模式后，无需重启项目即可实时修改代码
    # 出现bug时可直接观察出错部分
    
    # 2.修改host 
    # 作用：让其他电脑能够访问项目
    # 3.修改端口号
    
    if __name__== '__main__':
        # app.run(debug=True)   # debug模式开启
        # app.run(host='0.0.0.0',port = 9000) # 修改host和端口号
        app.run()
    ```
  
  ### url与视图映射
  
  - ```py
    from flask import Flask,request
    
    app = Flask(__name__)
    
    # 定义url http[80]/https[443]://www.qq.com/ path
    
    @ app.route('/')
    def helloworld():
        return "hello world!"
    
    @ app.route("/profile")     # 记得双引号
    def profile():
        return "个人中心"
    
    @ app.route("/blog/<blogid>")   # 带参数的url,<int:blogid>
    def blog_id(blogid):
        return "博客：%s" %blogid
    
    # /book/list 返回第一页的图书列表
    # /book/list?page=2 返回第二页图书列表
    @ app.route("/book/list")
    def book_list():            # 引入request
        # request.args.get("key",默认值，类型)  参数
        page = request.args.get("page",default = 1,type = int)
        return f"获取的是{page}页的图书列表"
    
    if __name__== '__main__':
        app.run(debug=True)
    ```
  
  ### 模版渲染
  
  - ```py
    from flask import Flask,render_template
    
    app = Flask(__name__)
    
    
    @ app.route('/')
    def helloworld():
        return  render_template("index.html")   #依据html文件渲染主页
    
    @ app.route("/blog/<blogid>")
    def blog_id(blogid):
        return render_template("index.html",blogid_html = blogid)    # 对html文件传参，在html中体现为{{ blogid_hmtl }}
    
    
    if __name__== '__main__':
        app.run(debug = True)
    ```
  
  ### 模版访问对象属性
  
  ```py
  from flask import Flask,render_template
  
  app = Flask(__name__)
  
  class user:
      def __init__(self,name,email):
          self.name = name
          self.email = email
  
  @ app.route('/')
  def helloworld():
      user(name = "ggg",email = "ds@qq.com")  #user的初始化
      person = {          # 字典
          "name" : "zs",
          "email" : "zs.com"
      }
      return  render_template("index.html",user_html = user,person_html = person)   # 在html文件中体现为{{ user_html.name }} / {{ user_html.email }}
                                                                                  # 字典同理，person_html.name
  
  
  if __name__== '__main__':
      app.run(debug = True)
  ```
  
  ### 过滤器的使用
  
  ```py
  from flask import Flask,render_template
  
  app = Flask(__name__)
  
  class user:
      def __init__(self,name,email):
          self.name = name
          self.email = email
  
  @ app.route('/')
  def filter():
      user = user(name = "ggg",email = "fefe.com")
      return render_template("index.html",user_html = user)          # 在html文件中，|为过滤器，例如name|length直接返回长度
  # 此外，也可以自定义过滤器，app.add_template_filter(函数名字，过滤器的名字)
  
  if __name__== '__main__':
      app.run(debug = True)
  ```
  
  ### 控制语句
  
  ```py
  from flask import Flask,render_template
  
  app = Flask(__name__)
  
  class user:
      def __init__(self,name,email):
          self.name = name
          self.email = email
  
  @ app.route('/')
  def filter():
      user = user(name = "ggg",email = "fefe.com")
      return render_template("index.html",user_html = user)
  @ app.route('/control')
  def control():
      age = 17
      books = [{
          "作者":"xxxx",
          "图书名字":"sss"
              },{...}]
      return render_template("index.html",age_html = age,bokks_hmtl = books)     # 在html文件中体现为{% if age > 18 %}
                                                              #                     xxxxxx
                                                              #                  {% endif %}
                                                              #                 {% for book in books %}
                                                              #                 {% endfor %}
  if __name__== '__main__':
      app.run(debug = True)
  ```
  
  ### 模版继承
  
  - 直接在子html文件中添加{% extends "parent.html" %}
  - 需要修改的地方加入{% block title/body %}
  
  
  
  ### 加载静态库
  
  ```py
  from flask import Flask,render_template
  
  app = Flask(__name__)
  
  
  @ app.route('/')
  def helloworld():
      return "hello world!"
  
  @ app.route("/static")
  def static_demo():
      return render_template("index.html")    # 在html文件中体现为<img src = "{{url_for('static',filename = "xxx")}}">
                                              # 在引用css文件中体现为<link rel = "stylesheet" href = "{{url_for('static',filename = "xxxx")}}">
                                              # js同理
  if __name__== '__main__':
      app.run()
  ```