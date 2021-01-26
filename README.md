# dailyReportAutofilling
适用于T大在线信息服务平台（暂时）

### **NOTICE: 脚本仅供学习参考，信息需要更新填报~**

### 简介
- 使用selenium编写的Python脚本，可以在T大信息服务平台上自动填写日报表
- 配合任务定时执行功能（如Win10“任务计划程序”），可以做到每日定时自动填写
- 代码仅供学习参考，一定要认真填写报表！！（特别是信息变动的时候）

### 运行环境与启动
- 环境
  - Python 3及以下packages
    - selenium （核心，用于浏览器调试操作）
    - numpy和pandas（数据操作）
  - Chrome 和对应版本的ChromeDriver（可以百度下载），ChromeDriver需要配置到环境变量中
  
  
 - 运行方法
 1. 将Python和ChromeDrive配置到环境变量
 2. 终端分别输入python/chromedrive，检查是否配置成功
 3. 安装selenium等包
 4. 运行脚本`python <.py>`测试，总时间视网速而定。若最后一行输出"Success！"，且很快收到微信通知，即运行成功
 5. 可以在定时执行任务的程序中设置python定时执行，使用该脚本路径作为参数
 
