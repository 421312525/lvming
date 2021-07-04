'''
@author:lvming
@time:2021/6/23
'''
import json
import random


def lottery():
    str='A0324 A0321 AA0314 A0121 A0344 A0361 A0311 A0121 A0244 A0325 A0234 A0120 ' \
        'A0310 A0318 A0343 A0333 A0332 A0242 A0112 A0542 A0211 A0343 A0644 A0125 '
    str1=str.replace(' ','')
    names=str1.split('A')
    for name in names:
        if name == '':
            names.remove(name)

    return names


list=lottery()
'''
一等奖 1
二等奖 3
三等奖 8
'''
choice = random.sample(list,3)
choice = json.dumps(choice,ensure_ascii=False)
print('中奖者：'+choice)