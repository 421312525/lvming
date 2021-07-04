'''
@author:lvming
@time:2021/7/1
'''
# JsonPath
'''
    JsonPath模块，是一个专门用于处理Json字符串的模块，JsonPath相当于xpth
    部署JsonPath，通过pip install jsonpath来进行安装
    通过jsonpath获得的内容，会以list的形式进行返回，也就意味着你的jsonpath是可以有一个值或者多个字同时存在的
    如果要基于jsonpath来处理json数据， 就一定要同步去处理list
    
    如果要基于JsonPath来处理json数据，就一定要同步去处理list
    JsonPath定义中，如果表达式出现错误，则会返回False(布尔类型的值)
    JsonPath要么返回False，要么返回获取的list
'''
import jsonpath,json

data = {

}

# 基于jsonpath获取元素 通过jsonpath函数来进行获取（json数据，定位表达式）
'''
    Jsonpath表达式的基本格式规范：
	$ 表示根节点，也是所有jsonpath的表达式的开始
	. 表示获取子节点
	.. 表示获取所有符合条件的内容
	* 表示所有的元素节点
    [] 表示迭代器的标示(可以用于处理下标等情况)
    [，] 表示多个结果的选择
    ?()表示过滤操作
    @表示当前节点

'''
bicycle = jsonpath.jsonpath(data,'$.store.bicycle')
print(bicycle[0]['color'])
# # 获取bicycle下的color
# bicycle = jsonpath.jsonpath(data,'$.store.bicycle.color')
print(bicycle)
book = jsonpath.jsonpath(data,'$.store.book')
print(book)
# 获取store下的所有price节点的值
price = jsonpath.jsonpath(data,'$.store..price')
print(price)
# 获取book下的所有price节点
book_price = jsonpath.jsonpath(data,'$.store.book..price')
print(book_price)
# 获取指定book下的price节点
book_price1 = jsonpath.jsonpath(data,'$.store.book[0].price')
print(book_price1)
book_price2 = jsonpath.jsonpath(data,'$.store.book[*].price')
print(book_price2)
book_price3 = jsonpath.jsonpath(data,'$.store.book[0,1].price')
print(book_price3)
# 获取price大于10的所有book
book_1 = jsonpath.jsonpath(data,'$..book[?(@.price>10)]')
print(book_1)

data = None
json.dumps(data)