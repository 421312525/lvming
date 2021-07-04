'''
@author:lvming
@time:2021/6/23
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
HTML基础知识：
   所有的元素定位归根结底都是在静态页面的操作下实现的。
   HTML叫做标签语言。基于不同的标签来展示不同的内容。
   常见的标签：
   a：超链接
   img：图片
   input：输入框、文件上传、按钮。。。
  iframe：窗体
  span、div
HTML标签内容，在展示的时候，不要被肉眼欺骗，要依据于class属性来确定元素长啥样，而操作的根本在于标签的名称。
标签包含有几个不同的特性需要了解：
1.标签名称，所有的标签都一定会有标签名
   标签名==元素
2.属性，单个标签可以有多个属性,只有在<>中的才叫做属性
<a attribute 1=“”></a>
<a attribute1=“”/>
3.文本，在<></>之间的内容，叫做文本
元素定位：
   提供有八种不同的元素定位方法。在Selenium的实现中，准确来说是有十六种不同的定位方法。(八种单数，八种复数)
   自动化中通过元素定位获取的对象都是WebElement对象。
   八种元素定位：(开发者工具中，elements标签页下，通过ctrl+F显示元素差找框)
	1.id：基于标签的id属性来进行定位,类似于身份证号码,基本不会重复，为了避免出现重复，最好是提前校验一下
	2.name：类似于身份证上的名字，容易重名
	3.link text 用于定位超链接(a标签),通过a标签的文本进行定位
	4.partial link text 用于定位a标签，通过模糊查找的形式来实现定位，类似于mysql中的like关键字
	一般partial_link_text定位会出现多元素的结果，一般可以通过find elements来进行定位。
        (1).不加s进行的定位，默认返回查找到的第一个元素
        (2).加s进行定位，基于下标的选择来返回元素
	5.tagname 基于标签名进行定位,一般而言不推荐，只有在特殊情况下需要用到
	6.classname 极其不推荐使用的元素定位方法,除非是实在没有办法了。
	7.cssselector 是定位界的万金油之一,专治IE浏览器下的元素定位疑难杂症,可以通过右键copy的形式来定位
	8.xpath 也是万金油,是基于树状结构来进行定位的，类似与文件机制
	    绝对路径：/html/body/div[1]/div[4]/div[1]/div[3]/div[3]/h3/a,绝对路径下的下标是从1开始
	    实在定位不到元素的时候，也不推荐使用。
        相对路径：有相对路径的语法来实现便捷的定位手段。
        //input[@id="kw"] 从跟路径下查找id为kw的input标签
        //*[@id="kw"]
        基本语法规则：
            // 从跟路径下开始查找，从html标签开始
            input 查找的元素标签名称，如果是*，表示查找全部的标签
            [] 添加筛选条件,可以但条件，也可以通过and进行多条件关联 
            //input[@type=“hidden” and name=“issp”]  通过and进行定位
            //form[@name=“f”]/input[5]   通过父元素下子元素的索引找子元素
            //input[@name="rsv_spt"]/..  通过子元素找父元素
            text() 固定写法，专属于通过text文本来查找元素的筛选条件，text内容完全符合一致才可以。
            //*[text()="新闻"]  找a链接，通过text文本
            @ 表示属性(Attribute)
        xpath中包含有非常多的元素定位方法，但是，基本上常用的就是一种，相对路径以及爸爸找儿子是最常用的
        在查找元素的时候，推荐是自上而下进行查找。
    xpath常用函数：
	    contains：通过模糊查找的行为，查找元素。可以通过属性或者文本作为查找条件
	        //a[contains(text(),"新")]
	        //input[contains(@id,"kw")]
	        //input[@id="kw" and contains(text(),"新")]
	    伪元素：(有些特定数据是在调用页面的时候才会进行接口通信生成的。)一般常见于下拉列表中
	        ::defor::
	        ::after::
	        遇到伪元素的时候，通过cssselector定位即可(find_element_by_css_selector)
   最为主流的定位方法是xpath，最灵活的定位方法是cssselector和xpath两种
'''
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 1.通过id来进行元素的定位
# el = driver.find_element_by_id('kw')

# 2.通过name来进行元素定位
# el = driver.find_element_by_name('wd')
# print(type(el))

# 3.通过link text进行元素定位
# el = driver.find_element_by_link_text('新闻')

# 4.通过partial_link_text进行元素定位
# el = driver.find_element_by_partial_link_text('百度')
# print(el.text)

# elements的定位默认返回一个list，将所有符合条件的元素全部放到一个list中，再将list返回
# el = driver.find_elements_by_partial_link_text('百度')
# for l in el:
#     print(l.text)

# 5.通过tagname进行定位:都是基于复数的s来定位
# el = driver.find_elements_by_tag_name('a')
# for l in el:
#     print(l.text)

# 6.通过classname进行定位:是通过标签的class属性定位,不推荐
# el = driver.find_element_by_class_name()

# 7.通过cssselector进行定位：
# el = driver.find_element_by_css_selector('#kw')

# 7.通过xpath进行定位：
el = driver.find_element_by_xpath('//input[@id="su"]')
# //input[@class="s_ipt"]
# driver.find_element_by_xpath()  #返回第一个
# driver.find_elements_by_xpath() #返回List

# 筛选器类实现八种不同的元素定位
# driver.find_element(By.XPATH,'//a[contains(text(),"新")]')
# By.XPATH == "xpath"
# driver.find_element("xpath",'//a[contains(text(),"新")]')

sleep(3)
driver.quit()