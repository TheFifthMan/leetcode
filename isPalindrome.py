# coding: utf-8 
# 题目要求
'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
'''
# 分析
'''
1. 负数肯定不是回文数

x =  121

x % 10 => 1
x = int(x / 10) => 12
-----------------------
x % 10  => 2
x = int(x / 10) => 1

'''

def isPalindrome(x):
    if x < 0 :
        return False
    rev = 0
    target = x
    while x!=0:
        pop = x % 10
        x =int(x / 10)
        rev = rev * 10 + pop

    
    if rev == target:
        return True
    else:
        return False

    
    
if __name__ =="__main__":
    for i in range(0,1000):
        if isPalindrome(i):print(i)
   
    
        
    