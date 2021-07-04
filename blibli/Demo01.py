'''
@author:lvming
@time:2021/6/17
'''
#算法
#递归的两个特点： 调用自身、结束条件
# def func3(x):
#     if x>0:
#         print(x)
#         func3(x-1)
# # func3(5)
# def func4(x):
#     if x>0:
#         func4(x-1)
#         print(x)
# func4(5)
# 递归实例：汉诺塔问题
# n=2时：
# 1.把小圆盘从A移动到B
# 2.把大圆盘从A移动到C
# 3.把小圆盘从B移动到C
# n个盘子时：
# 1.把n-1个圆盘从A经过C移动到B
# 2.把第n个圆盘从A移动到C
# 3.把n-1个小圆盘从B经过A移动到C
# def hanoi(n,a,b,c):
#     if n>0:
#         hanoi(n-1,a,c,b)
#         print('moving from %s to %s'%(a,c))
#         hanoi(n-1,b,a,c)
# hanoi(3,'A','B','C')

#查找
#查找：在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程。
#列表查找（线性表查找）：从列表中查找指定元素
#输入：列表、待查找元素
#输出：元素下标(未找到元素时一般返回None或-1)
#内置列表查找函数：index()

# 1.顺序查找
# 顺序查找：也叫线性查找，从列表第一个元素开始，顺序进行搜索，直到找到元素或搜索到列表最后一个元素为止。
# 时间复杂度：o(n)
def linear_search(li,val):
    for ind,v in enumerate(li):
        if v==val:
            return ind
    else:
        return None
# li=[1,2,3,4,5,6,7,8,9,10,12,12,12,1,23,1,41,42,1,41,23,1,2,41,41,42,1,312,3,1,1,412,3,13,1,3,1]
# a=linear_search(li,23)
# print(a)
#2.二分查找binary Searh
# 二分查找：又叫折半查找，从有序列表的初始候选区li[0:n]开始，通过对待查找的值与候选区中间值的比较，可以使候选区减少一半。
def binary_searh(li,val):
    left=0
    right=len(li)-1
    while left <= right:    #候选区有值
        mid=(left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]>=val:  #待查找的值在mid左侧
            right=mid-1
        else:   #li[mid]<=val   待查找的值在mid右侧
            left=mid+1
    else:
        return None
# lo=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# s=binary_searh(lo,18)
# print(s)

#排序
#排序：将一组”无序”的记录序列调整为”有序”的记录序列。
#列表排序：将无序列表变为有序列表
# 输入：列表
# 输出：有序列表
# 升序与降序
# 内置排序函数：sort()
'''
常见排序算法
排序low B三人组：
冒泡排序 选择排序 插入排序
排序NB三人组：
快速排序 堆排序 归并排序
其它排序：
希尔排序 计数排序 基数排序
'''
# 1.冒泡排序
# 列表每两个相邻的数，如果前面比后面大，则交换这两个数。
# 一趟排序完成后，则无序区减少一个数，有序区增加一个数。
# 代码关键点：趟、无序区范围
# 时间复杂度O(n*n)
# def bubble_sort(li):
#     for i in range(len(li)-1):  #第i趟
#         for j in range(len(li)-i-1):
#             if li[j]>li[j+1]:   #>升序  <降序
#                 li[j],li[j+1]=li[j+1],li[j]
#         print(li)
import random
# li=[random.randint(0,10000) for i in range(10)]
# print(li)
# bubble_sort(li)
# print(li)

# 优化冒泡排序
def bubble_sort(li):
    for i in range(len(li)-1):  #第i趟
        exchange=False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:   #>升序  <降序
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        print(li)
        if not exchange:
            return

# li=[9,8,7,1,2,3,4,5,6]
# li=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# bubble_sort(li)
# print(li)

#2.选择排序
# 一趟排序记录最小的数，放到第一个位置
# 再一趟排序记录记录列表无序区最小的数，放到第二个位置
# …..
# 算法关键点：有序区和无序区、无序区最小数的位置
# 简单版：会开辟新的列表，占用两份空间
def select_sort_simple(li):
    li_new=[]
    for i in range(len(li)):
        min_val=min(li)
        li_new.append(min_val)
        li.remove(min_val)
        # print(li_new)
    return li_new

def select_sort(li):
    for i in range(len(li)-1):  #  i是第几趟
        min_loc=i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]:
                min_loc = j
        if min_loc!=i:
            li[i],li[min_loc]=li[min_loc],li[i]
        print(li)

# li=[3,4,2,1,5,6,8,7,9]
# print(li)
# # print(select_sort_simple(li))
# select_sort(li)

# 3.插入排序
# 初始时手里(有序区)只有一张牌
# 每次(从无序区)摸一张牌，插入到手里已有牌的正确位置
# def insert_sort(li):
#     for i in range(1,len(li)):  # i 表示摸到的牌的下标
#         j=j-1   #j指的是手里的牌的下标
#         while

