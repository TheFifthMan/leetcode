# coding: utf-8 
# 题目
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''
# 分析
'''
target = 123
v1 = target % 10  # 3
v2 = target - v1  # 120
v3 = v2 / 10      # 12
# -------------------------
v4 = v3 % 10      # 2
v5 = v3 - v4      # 10 
v6 = v5 / 10      # 1

target = 234
v1 = target % 10  # 4
v2 = target - v1  # 230
v3 = v2 / 10      # 23
# ----------------------
v4 = v3 % 10      # 3
v5 = v3 - v4      # 20
v6 = v5 / 10      # 2


'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math 
        flag = 0 
        summary = 0
        if x > 0: flag = 1
        if x < 0: flag = -1 
        arr = []
        target = x * flag 
        while target >= 10:
            v1 = target % 10
            v2 = target - v1
            target = v2 / 10
            arr.append(v1)
        arr.append(target)
        arr.reverse()
        for i in range(0,len(arr)):
            print("index: ",i)
            print("value: ",arr[i])
            summary += arr[i]*math.pow(10,i)
            print(summary)
        
        result = int(summary * flag) 
        if result > math.pow(2,31)-1 or result < math.pow(-2,31):
            result = 0
        
        return result

# 官方解法：
class Solution2:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math 
        if x < 0:
            flag = -1
        elif x > 0:
            flag = 1
        else:
            flag = 0 
        
        target = x * flag 
        rev = 0
        
        while target!=0:
            pop = target % 10
            target = int(target / 10)
            rev = rev * 10 + pop
        
        if rev > math.pow(2,31)-1 or rev<math.pow(-2,31): return 0

        
        return rev * flag 
            