- urllib模块
    - 比较古老, 操作繁琐
- requests模块
    - python中原生的一款基于网络请求的模块, 功能强大, 简单便捷, 效率极高
    - 作用: 模拟浏览器发送请求.
    - 使用: (是浏览器获取数据的步骤, 也是requests模块的编码流程)
        - 指定url
        - 发起http或https请求(既可以是get, 也可以是post)
        - 获取响应数据(response)
        - 持久化存储

- 实战巩固
    - 需求: 爬取搜狗指定词条对应的搜索结果页面(简易网页采集器)
        - UA检测
        - UA伪装
    - 需求: 破解百度翻译
        - 可以直接使用数据解析来解析出页面局部的数据, 但是我们先使用ajax请求
        - ajax请求可以进行局部的页面刷新(在XHR中查看)
        - 分析得到: 使用了post请求(携带了参数), 响应数据是一组json数据
    - 需求: 爬取豆瓣电影分类排行榜 https://movie.douban.com/ 中的电影详情数据
        - 通过抓取首页url, 可以判断, 是动态加载数据
        - 首页中的信息是通过ajax请求得到的

    - 需求: 爬取药监总局各公司详情页的信息
      http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=ed59438f34ae47e794f4c7ee5137c1f7
      http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=5eb10afc74a2462c8e86652ec8d90a48
      http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=327b7ce0c2214b6ea502f5cb00c0d1a9
        - 通过对各公司详情页url的观察, 发现:
            - url的域名都是一样的, 只有id不同
            - id值可以从对应的ajax请求到的json字符串中获取
            - 域名和id值拼接到一起, 即可得到一个完整的企业对应的详情页url
        - 详情页的数据也是通过ajax请求动态请求到的
          http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
        - 观察发现:
            - 所有的post请求的url都是一样的, 只有参数id值是不同的
            - 如果我们可以批量获取多家企业的id, 就可以使用'id' + 'post请求的url', 批量获取多家企业的详情页信息

- 数据解析:
    - 聚焦爬虫(爬取一整张页面的局部内容, 先爬取一整张页面, 然后对这张页面的局部进行解析操作)
        - 解析操作:
            - 正则
            - bs4
            - xpath
