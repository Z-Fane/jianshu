# jianshu
基于scrapy-redis分布式爬取简书
# 简介
分布式使用redis实现，redis中存储了爬虫的request，stats信息，能够对各个机器上的爬虫实现集中管理，
这样可以 解决爬虫的性能瓶颈，利用redis的高效和易于扩展能够轻松实现高效率下载：当redis存储或者访问速度遇到瓶颈时，
可以通过增大redis集群数和爬虫集群数量改善。
# 避免爬虫被禁的策略
禁用cookie
实现了一个user_agents，不停的变user-aget

# 运行环境
- scrapy
- redis
- scrapy-redis
- python 3.6
- sqlyalchemy+mysql

# 运行截图
![jietu](/screenshots/20180601085022.png)
![jietu](/screenshots/20180601085131.png)





