# QAU-Reports
青岛农业大学QAU自动每日上报  
如果您的防疫信息出现变动，请务必及时更改脚本中所对应的参数。  
作者TG：[ialtone](https://t.me/ialtone)  欢迎交流。  
部分代码来源于[QAU-Auto-Information-Report](https://github.com/alexhoshina/QAU-Auto-Information-Report)

# 使用说明
## 部署到阿里云函数服务平台
点击进入[阿里函数计算官网](https://fcnext.console.aliyun.com/overview)
，登录后进入控制台。  
登录之后点击**服务及函数**，再点**创建服务**，填上名称点创建即可。  
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917150818.png)  
点击**创建函数**。  
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917151446.png)  
**创建方式**选择**从零创建**，**运行环境**选择**python**，**代码上传方式**选择**通过ZIP包上传代码**，然后把[Releases](https://github.com/ialtone/QAU-Reports/releases/download/1.0/QAU-Reposts.1.0.zip)(点击可跳转下载)压缩包上传即可。
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917151707.png)  
触发器类型选择定时触发器，触发方式选择指定时间，时区选择Asia/Shanghai(北京时间)，指定一个时间后点击创建。
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917152051.png)  
等待在线IDE启动后，打开config.json和User.json两个文件等待编辑。
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917152458.png)  
进入[QAU自动每日上报信息填写](http://qau.ialtone.xyz:8080/)(点击可跳转)，**红框框出来的项目切记填写**，其他信息可根据您的情况自行更改，也可保持默认。  
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917152612.png)  
如果您想要每天微信通知您自动每日信息上报是否运行成功的话，请将微信PushPlus通知开关打开，并填写您PushPlus的token。  
PushPlus的token获取方式为：  
微信搜索PushPlus，点击公众号并关注。  
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917153008.png)  
关注之后大多数情况下会直接发送给您token，复制到[QAU自动每日上报信息填写](http://qau.ialtone.xyz:8080/)token的地方即可。  
如果未发送token给您，请点开功能里的个人中心。  
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917153240.png)  
打开之后点击登录，再点击开发设置，再点击Token即可一键复制您的token。  
信息填写完成之后点击提交按钮将会跳转到如下界面。
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917154148.png)  
将上面红框里的内容复制到阿里云函数在线IDE中刚刚打开的config.json和User.json中并保存。  
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917154453.png)  
确保刚刚的内容复制过去之后点击部署代码，再点击测试代码，如果您打开微信PushPlus的话约五秒钟后将会收到通知，出现'每日上报失败！'的提醒请您不要惊慌，这是因为您今天已经上报。
![](https://cdn.staticaly.com/gh/ialtone/ialtone@master/图床20220917154642.png)  
当完成上述所有步骤后，恭喜您成功部署了QAU-Reports。  
觉得项目对您有用的话，您的Stars将是对我最大的支持。  
## 部署到服务器  
待完善。