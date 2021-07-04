'''
@author:lvming
@time:2021/7/1
'''
# MockServer 实现Mock的数据生成与调用
'''
    MockServer：
   接口在系统中分为内部接口与外部接口两种类型。
   自主研发的叫做内部接口
   别人做好的叫做外部接口
   例如：
	在测试支付的时候，必须要实际转入金钱次啊可以实现数据的交互与测试
	假装支付成功，生成一串伪数据，完全遵循支付的返回结果
	例如：支付返回结果{
	result：1
	money：0.01
}
{
	result：0
	money：0.01
}
    伪造之后，将伪造的数据与内部接口继续进行通信
    伪造的技术叫做Mock Server，数据的生成和提供
    
    前端要交互数据，需要关联到后端的接口
    后端的接口在未实现完成时，也可以通过Mock来进行数据提供
    测试中，如果关联到部分没有必要一直调用的接口时，可以直接通过mock来实现
    Mock本意就是定义了一个返回结果，与变量赋值形态的区别
    Mock需要定义到制定的接口作为对象
    
    # 课后作业：
        # 1.熟悉md5加密的流程，并实现封装
        # 2.熟悉mock的应用，并实操本节课的课堂代码
        # 3.选修题：自行研发一套md5解密的算法。支持cv，大那是要解释解密过程
'''
from unittest import mock

# 伪造一个接口数据
def plus(a,b):
    # return a+b
    '''
    :param a: int
    :param b: int
    :return: a+b
    '''
    pass
def math():
    b = plus(1,2)
    print('math:{0}'.format(b))
    return b
def login():
    pass

# print(plus(1,2))
# 对指定的接口进行mock值的生成
'''
    mock.Mock，定义函数的返回值，无关乎函数本身内容，直接写入最终的返回结果
'''
# plus = mock.Mock(return_value=10)
# plus = mock.Mock(return_value=Exception)
# plus(1,2)
# print(plus(1,2))