'''
@author:lvming
@time:2021/6/28
'''
from pom.base_page.base_page import BasePage

'''
    CartPage:购物车页面，校验商品是否添加成功
'''

# 购物车页面
class CartPage(BasePage):
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/cart/index.html'

    goods = ('xpath','//a[contains(text(),"iPhone")]')

    # 校验购物车商品是否存在
    def cart_info(self):
        self.visit(self.url)
        self.wait(self.goods)
        # return self.assert_text(self.goods,'iPhone')